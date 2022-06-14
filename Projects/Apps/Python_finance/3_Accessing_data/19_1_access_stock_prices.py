import yfinance as yf
import matplotlib.pyplot as plt


data = yf.Ticker("TSLA")
data.history(period="5d")
data.history(start="2021-06-21", end="2021-12-06")
print(data.history())
print()


data = yf.Ticker("TSLA")
x = data.history()["Close"]
x.plot
print()


data = yf.Ticker("TSLA")
x = data.history("3mo")["Close"]
print(x.mean())
print()


data = yf.download("AAPL MSFT TSLA", start="2021-01-01")
print(data["Close"])
data["Close"].plot()
print()