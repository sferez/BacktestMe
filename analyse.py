#analyse.py

import pandas as pd

df=pd.read_csv("data.csv", encoding="utf8")
df["asset"]=df["asset"].astype("string")
df["timeframe"]=df["timeframe"].astype("string")
assets=["BTCUSDT","ETHUSDT"]
timeframes=["1d","4h","1h","30m","15m","5m"]


for asset in assets:
    print("***************"+asset+"***************")
    for timeframe in timeframes:
        print("--------------"+timeframe+"--------------")
        print("moyenne "+asset+" & timeframe "+timeframe+" : " +str(df[df["asset"]==asset][df["timeframe"]==timeframe]["edge"].mean()))
        print("ecart type "+asset+" & timeframe "+timeframe+" : " +str(df[df["asset"]==asset][df["timeframe"]==timeframe]["edge"].std()))
        print("max "+asset+" & timeframe "+timeframe+" : " +str(df[df["asset"]==asset][df["timeframe"]==timeframe]["edge"].max()))
        print("min "+asset+" & timeframe "+timeframe+" : " +str(df[df["asset"]==asset][df["timeframe"]==timeframe]["edge"].min()))
        print("Q1 "+asset+" & timeframe "+timeframe+" : " +str(df[df["asset"]==asset][df["timeframe"]==timeframe]["edge"].quantile(0.25)))
        print("mediane "+asset+" & timeframe "+timeframe+" : " +str(df[df["asset"]==asset][df["timeframe"]==timeframe]["edge"].quantile(0.5)))
        print("Q3 "+asset+" & timeframe "+timeframe+" : " +str(df[df["asset"]==asset][df["timeframe"]==timeframe]["edge"].quantile(0.75)))




