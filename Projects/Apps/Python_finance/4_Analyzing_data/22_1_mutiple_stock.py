import yfinance as yf
import numpy as np
import pandas as pd


data = yf.download("AAPL MSFT TSLA", start="2021-01-01")
x = data["Close"].pct_change()
print(x)
print()

# x = yf.download("AAPL MSFT TSLA", start="2020-07-01", end="2021-07-01")


data = yf.download("AAPL MSFT TSLA", start="2021-01-01")
x = data["Close"].pct_change()
print(x.describe())
print()



data = yf.download("AAPL MSFT TSLA", start="2021-01-01")
data["Close"].plot()
x = data["Close"].pct_change()
x.plot()
x = data["Close"].pct_change()
(x + 1).cumprod().plot()
print()