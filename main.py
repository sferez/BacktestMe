#main.py

import pandas as pd
import mplfinance
import getdata
import indicators
import strategy
import show
import time

data=[]
sma1s=range(5,100)
sma2s=range(10,200)
assets=["ETHUSDT","BTCUSDT"]
timeframes=["1d","4h","1h","30m","15m","5m"]


for asset in assets:
    print("--------START "+str(asset)+"----------")
    for timeframe in timeframes:
        print("--------START "+str(timeframe)+"----------")
        dfp=pd.DataFrame(getdata.get_data(asset,timeframe,"2015,1,1"))
        for sma1 in sma1s:
            print("*") 
            for sma2 in sma2s:

                if sma1>sma2:
                    continue

                df=dfp.copy()

                df=indicators.logreturn(df)
                df=indicators.Sma(df,sma1)
                df=indicators.Sma(df,sma2)
                df=strategy.strategyLong(df,sma1,sma2)
                df=strategy.strategyShort(df,sma1,sma2)



                # show.show(df,sma1,sma2)
                perf=indicators.performance(df)

                data.append({
                    "asset":asset,
                    "timeframe":timeframe,
                    "sma1":sma1,
                    "sma2":sma2,
                    "edge":perf,
                    "edgeLong":indicators.performanceLong(df),
                    "edgeShort":indicators.performanceShort(df),
                })  
        print()
        print("--------"+str(timeframe)+" DONE----------")
        print("--------CHANGE TIMEFRAME----------")
    print("--------"+str(asset)+" DONE----------")
    print("$$$$$$$ CHANGE COIN $$$$$$$$$$")

print(data)

data=pd.DataFrame(data)
data.to_csv("data.csv" ,encoding="utf8")