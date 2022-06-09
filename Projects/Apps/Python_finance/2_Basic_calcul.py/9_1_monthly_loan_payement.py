import numpy_financial as npf

res = npf.pmt(rate=0.07/12, nper=5*12, pv=100000, fv=0)
print(res)
print()

res = npf.pmt(rate=0./12, nper=5*12, pv=0, fv=50000)
print(res)
