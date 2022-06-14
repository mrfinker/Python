import yfinance as yf
import pandas as pd
import numpy as np


data = yf.Ticker("TSLA")
price = data.history(period="1y")
x = price["Close"].pct_change()
print(x)
print()


x = price["Close"].pct_change()
x.plot()
x.plot(kind="hist")
print()


x = price["Close"].pct_change()
returns = (x + 1).cumprod()
returns.plot()
print()


x = np.array([2,4,2])
r = x.cumprod()
print(r)
