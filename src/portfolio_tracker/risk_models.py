from typing import Tuple
import numpy as np
import pandas as pd


def realized_vol(daily_ret: pd.Series, window: int = 5, annualized: bool = True) -> pd.Series:
    """
    Rolling realized volatility over a given window of specified length
    
    Parameters 
    ----------
    daily_ret : pd.Series
        Daily portfolio returns.
    window : int
        number of days in the volatility window
    annualize : bool
        If true, scale by swrt(252) to annualize.
    
    
    Returns a pd.Series -> Rolling volatility series (aligned with the end of each window)
    
    """

    vol = daily_ret.rolling(window).std(ddof=0) #this function basically takes a window of return from the serie created by daily ret, and compute the volatility for it
    if annualized:
        vol = vol * np.sqrt(252)
    return vol

def build_vol_dataset(port_ret: pd.Series, vol_windows=(5, 10, 20), ret_windows=(1, 5, 10),horizon: int = 5) -> Tuple[pd.DataFrame, pd.Series]:
   
    """ 
   Build feature matrix X and target y for next-week volatility prediction.

    Features (X):
      - past realized volatilities over windows in vol_windows
      - past cumulative returns over windows in ret_windows

    Target (y):
      - realized volatility over the *next* horizon days.
    """
    port_ret = port_ret.sort_index() #to make sure my return are well sorted
    feats = pd.DataFrame(index=port_ret.index) #create emptydataframe

    for w in vol_windows: #for each windows or daays
        vol_w = realized_vol(port_ret, window=w, annualized=True) #compute volatility over the windows w
        feats[f"rv_{w}d"] = vol_w #then store it in the dataframe "feats"

    for w in ret_windows: #same as vol but does the average of the given window of days
        cumret = port_ret.rolling(w).sum()
        feats[f"ret_{w}d_sum"] = cumret
        
    future_vol = (
        port_ret.rolling(horizon).std(ddof=0).shift(-(horizon - 1)) * np.sqrt(252) #create tyarget volatility based on the nest five days vol
    ) #it also place the target at the right date in the tbale so it's for the right expected future date
    y = future_vol.rename(f"rv_next_{horizon}d")

    data = feats.join(y, how="inner") #mix both features and target 
    data = data.dropna(how="any") #eliminate the one with NaN as entry (basically the one where we can't compute based on the horizon)

    X = data.drop(columns=[y.name])
    y = data[y.name]

    return X, y