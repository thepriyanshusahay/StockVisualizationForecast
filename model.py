# The dependencies...

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf

#code

df = yf.Ticker("MSFT")
df = df.history(period="1y")
df = df[['Close']]
forecast_out = 30
df['Prediction'] = df[['Close']].shift(-forecast_out)
X = np.array(df.drop(['Prediction'],1))
X = X[:-forecast_out]
Y = np.array(df['Prediction'])
Y = Y[:-forecast_out]
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2)
svr_rbf = SVR(kernel = 'rbf', C=1e3,gamma = 0.1)
svr_rbf.fit(x_train,y_train)
svm_confidence = svr_rbf.score(x_test,y_test)
lr = LinearRegression()
lr.fit(x_train,y_train)
lr_confidence = lr.score(x_test,y_test)
x_forecast = np.array(df.drop(['Prediction'],1))[-forecast_out:]
svm_prediction = svr_rbf.predict(x_forecast)
print(svm_prediction)
date =dt.datetime.now()
date1 =date.strftime("%x")
times = pd.date_range(date1, periods=forecast_out, freq='1d')
dff = pd.DataFrame(list(zip(times,svm_prediction)),
               columns =['Date', 'Prediction'])

print(lr_confidence)               