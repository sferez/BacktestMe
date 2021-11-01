#indicators.py

import pandas as pd
import numpy as np
from ta import trend


def Sma(df,sma):

    # df["SMA"+str(sma)]=df["Close"].rolling(sma).mean()
    df["SMA"+str(sma)]=trend.sma_indicator(df["Close"],window=sma)
    df=df.dropna()

    return df

def logreturn(df):
    
    df["logret"]=np.log(df.Close.pct_change()+1)
    return df

def performance(df):
    
    
    perf=np.exp(df[["logret","stratretLong","stratretShort"]].sum())
    perf["delta"]=perf["stratretLong"]+perf["stratretShort"]-perf["logret"]

    return perf["delta"]

def performanceLong(df):
    
    
    perf=np.exp(df[["logret","stratretLong"]].sum())
    perf["delta"]=perf["stratretLong"]-perf["logret"]

    return perf["delta"]

def performanceShort(df):
    
    
    perf=np.exp(df[["logret","stratretShort"]].sum())
    perf["delta"]=perf["stratretShort"]-perf["logret"]

    return perf["delta"]

def perf(df):
    perf=np.exp(df[["logret"]].sum())
    return perf

def perfShort(df):
    perf=np.exp(df[["stratretShort"]].sum())
    return perf

def perfLong(df):
    perf=np.exp(df[["stratretLong"]].sum())
    return perf