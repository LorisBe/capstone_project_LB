import sys
from pathlib import Path

# Make sure Python sees the project root so "src" is importable
ROOT = Path(__file__).resolve().parents[2]  # -> /files/capstone_project_LB
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


import pandas as pd
from typing import List, Dict, Optional
import yfinance as yf


from src.portfolio_tracker.io import fetch_prices
from src.portfolio_tracker.transform import portfolio_returns
from src.portfolio_tracker.kpis import kpi_table
from src.portfolio_tracker.risk_models import build_vol_dataset

def ask_position() -> Optional[Dict]:
    """
    This function as the user for his porfolio's position. (ticker, quantity, avg_cost, etc..)
    Return a dict for the position, or None if the user wants to stop
    """
    ticker = input("Ticker (empty to finish): ").strip() #ask him for the ticker
    if ticker == "" :
        return None
    
    qty_str = input("  Quantity: ").strip()
    cost_str = input("  Average cost per unit: ").strip()
    asset_type = input("  Asset type [default: Equity]: ").strip() or "Equity" #ask about all the detail of the position
    currency = input("  Currency [default: USD]: ").strip() or "USD"

    try:
        quantity = float(qty_str)
        avg_cost = float(cost_str) #See if cost and quantity are float, else re do it 
    except ValueError:
        print(" Quantity and average cost must be numbers. Try again.\n")
        return ask_position()

    pos = {
        "account_id": "acc1",          # simple default
        "asset_type": asset_type,
        "ticker": ticker,
        "currency": currency.upper(), 
        "quantity": quantity,
        "avg_cost": avg_cost,
    }
    return pos #return a dictionnary for that single position -> will be looped in future function to create multiple

def ask_holdings() -> pd.DataFrame:
    """
    Loop call of ask_position() until user stops, then build and return a holdings DataFrame
    """
    rows: List[dict] = []
    i = 1
    
    while True:
        print(f"Position #{i}") #use the last function unitl user breaks
        pos = ask_position()
        if pos is None: #user finished his holdings
            break
        rows.append(pos)
        i+= 1
        print()
        
    if not rows:
        raise ValueError("No positions entered")
    
    df = pd.DataFrame(rows)
    print("Holdings caputred, DataFrame of holdings created, please check accruacy:")
    print(df)
    return df

def fetch_prices_from_holdings(holdings: pd.DataFrame, start="2020-01-01", end=None):
    """
    Fetch price data for the tickers in holdings.
    Always returns a clean DataFrame: index = dates, columns = tickers,
    values = adjusted close prices.
    """

    tickers = holdings["ticker"].astype(str).unique().tolist()
    if not tickers:
        raise ValueError("No tickers in holdings.")

    print(f"\nFetching prices for tickers: {tickers}")

    data = yf.download(
        tickers=tickers,
        start=start,
        end=end,
        auto_adjust=True,      # already adjusted (dividends, splits)
        progress=False
    )

    # Case 1: MultiIndex (most common with >1 tickers)
    if isinstance(data.columns, pd.MultiIndex):
        if "Adj Close" in data.columns.levels[0]:
            data = data["Adj Close"]        # keep only adjusted close
        elif "Close" in data.columns.levels[0]:
            data = data["Close"]            # fallback
    
    # Case 2: Single-index for 1 ticker
    else:
        if "Adj Close" in data.columns:
            data = data[["Adj Close"]]
        elif "Close" in data.columns:
            data = data[["Close"]]
        # rename column to the ticker name
        data.columns = tickers

    # Clean-up
    data = data.sort_index().ffill().dropna(how="all")
    data.attrs["source"] = "yfinance"

    print("Prices downloaded (head):")
    print(data.head())

    return data
