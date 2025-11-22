import pandas as pd
from typing import List, Dict, Optional
import yfinance as yf


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

def fetch_prices(
    holdings: pd.DataFrame,
    start: str = "2023-01-01",
    end: Optional[str] = None,
) -> pd.DataFrame:
    """
    Fetch historical prices for all tickers in the holdings DataFrame
    using yfinance. Returns a DataFrame of adjusted close prices.
    """
    tickers = holdings["ticker"].astype(str).unique().tolist()
    if not tickers:
        raise ValueError("No tickers found in holdings.")

    print(f"\nFetching prices for: {tickers}")
    
    data = yf.download(
        tickers,         
        start=start,
        end=end,
        auto_adjust=True,
        progress=False,
    )

    # MultiIndex case: ('Adj Close', ticker)
    if isinstance(data.columns, pd.MultiIndex):
        if "Adj Close" in data.columns.levels[0]:
            data = data["Adj Close"]

    # Single-level case with 'Adj Close'
    if isinstance(data, pd.DataFrame) and "Adj Close" in data.columns:
        data = data["Adj Close"]

    # Ensure we always return a DataFrame
    if isinstance(data, pd.Series):
        data = data.to_frame()

    print("\n✅ Prices downloaded (head):")
    print(data.head())
    return data

if __name__ == "__main__":
    # Simple manual test
    print("\n=== Manual Input Test ===")
    try:
        holdings_df = ask_holdings()
    except Exception as e:
        print(f"\n❌ Error while entering holdings: {e}")
        raise SystemExit(1)

    print("\n=== Final Holdings DataFrame ===")
    print(holdings_df)


    try:
        prices_df = fetch_prices(holdings_df, start="2023-01-01")      #try to fetch prices with yfinance
        print("\n=== Final Prices DataFrame (head) ===")
        print(prices_df.head())
    except Exception as e:
        print(f"\n⚠️ Could not fetch prices: {e}")

    print("\n=== Program finished ===")
    