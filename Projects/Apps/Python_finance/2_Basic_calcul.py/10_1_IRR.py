import numpy_financial as npf

cashflow = [-5000, 500, 700, 1000, 3000]
res = npf.irr(cashflow)
print(res)

cf1 = [-50000, 10000, 25000, 25000, 35000, 42000]
cf2 = [-30000, 10000, 13000, 18000, 25000, 20000]
print("option 1 : ", npf.irr(cf1))
print("option 2 : ", npf.irr(cf2))
print()

cf3 = [-1, 1]
print(npf.irr(cf3))
