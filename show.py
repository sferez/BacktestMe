#show.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def show(df,sma1,sma2):
    fig,ax=plt.subplots()
    ax2=ax.twinx()
    ax.plot(df[["Close","SMA"+str(sma1),"SMA"+str(sma2)]])
    ax2.plot(df[["Long","Short"]])
    plt.show()

def showrelprofit(df):
    show=np.exp(df[["logret","stratretLong","stratretShort"]].cumsum())
    show["stratret"]=show["stratretLong"]+show["stratretShort"]-1
    fig,ax=plt.subplots()
    ax.plot(show)
    plt.yscale("log")
    ax.legend(show.keys())
    plt.show()