import matplotlib
import yfinance as yf
import matplotlib.pyplot as plt


data = yf.Ticker("TSLA")
print(data.info)
print(data.info["profitMargins"])
print(data.info["returnOnEquity"])
print()


print(data.dividends) #show dividendes
print(data.splits) #show splits
print(data.balance_sheet) #show balance sheet
print(data.cashflow) #show cashflow
print(data.earnings) #show earnings
print()


data = yf.Ticker("TSLA")
x = data.earnings
x.plot(kind="bar")