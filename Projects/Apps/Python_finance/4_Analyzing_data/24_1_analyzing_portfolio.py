import yfinance as yf
import numpy as np

stocks = ["AAPL", "AMZN", "MSFT", "TSLA"]
weights = [0.3, 0.2, 0.4, 0.1]
data = yf.download(stocks, start="2021-01-01")
#daily returns

x = data["Close"].pct_change()

#portfolio return
ret = (x * weights).sum(axis = 1)

#total cumulative returns for our portfolio
cumulative = (ret + 1).cumprod()
cumulative.plot()
print()


print(np.std(ret))
annual_std = np.std(ret)*np.sqrt(252)
print()


sharpe = (np.mean(ret)/np.std(ret))*np.sqrt(252)