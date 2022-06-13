import yfinance as yf


data = yf.Ticker("TSLA")
print(data.major_holders)
data.institutional_holders
print()

x = data.recommendations
x = x[x.index>"2021-06-01"]
print(x)
print()

def RoE(ticker):
    data = yf.Ticker(ticker)
    roe = data.info["returnOnEquity"]
    name = data.info["shortName"]
    print(name, ":", roe)

RoE("AAPL")
RoE("MSFT")
print()
