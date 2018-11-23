import pandas as pd
import quandl
import math
df=quandl.get('WIKI/GOOGL')
df=df[['Open','Adj. Close','Close','Adj. Volume']]
df['HL_PCT']=(df['Open']-df['Close'])/100;
df['PCT_CHANGE']=(df['Open']-df['Close'])/100;
df=df[['Adj. Close','HL_PCT','PCT_CHANGE']]
forecast_col='Adj. Close'
df.fillna(-9999,inplace=True);
forecast_out=int(math.ceil(0.1*len(df)))
df['label']=df[forecast_col].shift(-forecast_out)
print(df.head())


