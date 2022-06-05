import numpy_financial as npf

res = npf.fv(rate = 1, nper = 1, pmt = 0, pv = -100)
print(res)
print()

res = npf.fv(rate = 1, nper = 20, pmt = 0, pv = -1)
print(res)