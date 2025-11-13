import numpy as np
import pandas as pd

def annualize_vol(daily_ret: pd.Series) -> float:
    """Annualized volatility = daily std * sqrt(252).""" 
    return float(np.sqrt(252) * daily_ret.std(ddof=0)) #calculate the annual volatilty based on the 252 open day of trading (does not adjust for crypto)

def sharpe(daily_ret: pd.Series, rf_daily: float = 0.02) -> float: #Rf initated as 2%
    """Annualized Sharpe ratio using daily returns."""
    excess = daily_ret - rf_daily
    denom = excess.std(ddof=0)
    return float(np.sqrt(252) * excess.mean() / (denom)) 

def drawdown(equity_curve: pd.Series) -> pd.Series:
    """Calculate how much the portfolio has fallen from its highest value"""
    peak = equity_curve.cummax() #find the peak
    return (equity_curve - peak) / peak

def kpi_table(port_ret: pd.Series) -> pd.DataFrame: #gives me a data frame so it's nice and cleannnnn
    """Summarize key performance indicators."""
    eq = (1 + port_ret).cumprod() #equity curve
    dd = drawdown(eq) #compute drawdown
    return pd.DataFrame({ #build a dataframe to visualize all that
        "Cumulative Return": [eq.iloc[-1] - 1],
        "Ann. Vol": [annualize_vol(port_ret)],
        "Sharpe": [sharpe(port_ret)],
        "Max Drawdown": [dd.min()],
    })
