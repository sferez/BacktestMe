#test.py
import indicators
import strategy
import show
import pandas as pd
import getdata

dfp=pd.DataFrame(getdata.get_data("BTCUSDT","30m","2018,1,31"))

sma1=36
sma2=48

df=dfp.copy()
df=indicators.logreturn(df)
df=indicators.Sma(df,sma1)
df=indicators.Sma(df,sma2)
df=strategy.strategyLong(df,sma1,sma2)
df=strategy.strategyShort(df,sma1,sma2)


show.showrelprofit(df)

show.show(df,sma1,sma2)
print("edge : "+str(indicators.performance(df)))
print("edge Long : "+str(indicators.performanceLong(df)))
print("edge Short : "+str(indicators.performanceShort(df)))
print("perf : "+str(indicators.perf(df)))
print("perf Short : "+str(indicators.perfShort(df)))
print("perf Long : "+str(indicators.perfLong(df)))

print(strategy.nbrposition(df))