import pandas as pd

price = [42.5, 102.03, 240.38, 80.9]
s = pd.Series(price)
print(s.describe())
print()

x = [4,5,2,1]
s = pd.Series(x)
print(s[3])
print()

data = {
    "date" : ["2021-06-10", "2021-06-11", "2021-06-12", "2021-06-13"],
    "prices" : [42.5, 102.03, 240.38, 80.9]
}

df = pd.DataFrame(data)
print(df)
print()

donner = {
    "id":[42,8,54],
    "name":["A","B","C"]
}
df = pd.DataFrame(donner)
print(df)