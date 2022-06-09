import numpy_financial as npf

res = npf.fv(rate = 0.08, nper = 5, pmt = 0, pv = -1000)
print(res)
print()

rs = npf.pv(rate = 0.10, nper = 8, pmt = 0, fv = 1000)
print(rs)
print()

ris = npf.pv(rate = 0.07, nper = 15, pmt = 0, fv = 150000)
print(ris)
