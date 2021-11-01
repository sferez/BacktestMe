#strategy.py

import numpy as np
import pandas as pd

def strategyLong(df,sma1,sma2):

    df["Long"]=np.where((df["SMA"+str(sma1)]>df["SMA"+str(sma2)]),1,0)
    df["stratretLong"]=df["Long"].shift(1)*df["logret"]
    # (df["SMA"+str(sma1)]>df["SMA"+str(sma2)])
    
    df=df.dropna()
   
    return df

def strategyShort(df,sma1,sma2):

    df["Short"]=np.where((df["SMA"+str(sma1)]<df["SMA"+str(sma2)]),-1,0)
    df["stratretShort"]=df["Short"].shift(1)*df["logret"]
    # (df["SMA"+str(sma1)]<df["SMA"+str(sma2)])
    df=df.dropna()
   
    return df


def nbrposition(df):
    nbr=0
    for i,longs in enumerate(df["Long"]):
        if df["Long"][i-1]!=df["Long"][i]:
            nbr=nbr+1
    return nbr

