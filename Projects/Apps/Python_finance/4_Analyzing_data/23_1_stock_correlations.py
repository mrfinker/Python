import yfinance as yf
import statsmodels.api as sm



data = yf.download("FB AMZN AAPL NFLX GOOG", start="2020-01-01")
x = data["Close"].pct_change()
corr=x.corr()
print(corr)

sm.graphics.plot_corr(corr,xnames=list(x.columns))
# parfaitement correler est 1, et ici il n'y a que des valeurs entre 1 et -1