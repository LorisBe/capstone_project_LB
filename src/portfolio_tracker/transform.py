import pandas as pd
import numpy as np

def daily_returns(price_wide: pd.DataFrame) -> pd.DataFrame:
    """Percent change of adjusted close prices by column (ticker)."""
    return price_wide.sort_index().pct_change().dropna(how="all")

def portfolio_returns(holdings_df: pd.DataFrame, price_wide: pd.DataFrame) -> pd.Series:
    """
    Value-weighted portfolio daily returns.
    Weights computed once from quantities × first available prices.
    """
    prices = price_wide.sort_index().ffill() #initate price variable and sort it by index
    first = prices.iloc[0] #get the initial price
    shares = holdings_df.set_index("ticker")["quantity"].reindex(prices.columns).fillna(0.0) # Get quantities from holdings, align with tickers in price table
    values0 = shares * first # Compute total initial value (quantity × first price)
    total0 = float(values0.sum())
    if total0 <= 0:
        raise ValueError("Initial portfolio value is zero—check quantities and tickers.") #raise an error if the value is zero or below
    weights = values0 / total0 # Compute total initial value (quantity × first price)
    rets = daily_returns(prices).fillna(0.0) # Compute daily returns for each ticker
    port_ret = (rets * weights).sum(axis=1)  # Portfolio daily return = sum of (asset returns × weights)
    port_ret.name = "portfolio"
    return port_ret
#The portfolio_returns() function combines all my holdings and price data to compute a single series of daily portfolio returns. It uses fixed weights based on the initial value of each position and sums the weighted asset returns every day. This series is the foundation for all subsequent analytics (KPIs, drawdown, and machine learning forecasts).