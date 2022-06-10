import pandas as pd

data = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
df = data[0]
print(df)
print()
print()


data = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
df = data[0]
df = df[["Symbol", "Security"]]
print(df)
print()
print()

df = df[df["Security"] == "Apple"]
df.info()
print()
print()

res = data[data["Age"] > 18]