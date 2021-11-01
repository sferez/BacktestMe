#GetData.py

from numpy import fromiter
import pandas as pd
from binance.client import Client
import secret

def get_data(asset, timeframe, start, end="Today"):
    
    api_key=secret.api_key
    secret_key=secret.secret_key
    client=Client(api_key,secret_key)

    df = pd.DataFrame(client.get_historical_klines(asset,timeframe,start,end))

    df=df.iloc[:,:6]
    df.columns=["Date","Open","High","Low","Close","Volume"]
    df=df.set_index("Date")
    df.index=pd.to_datetime(df.index,unit="ms")
    df=df.astype("float")

    return df
