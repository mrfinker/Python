import numpy_financial as npf
import matplotlib.pyplot as plt
import numpy as np


print(npf.fv(rate = 0, nper=3, pmt=0, pv=-100))
print()

print(npf.pmt(rate=0.10/12, nper=5*12,pv=0,fv=50000))
print()

rev=[1800,2500,2000,4500]
plt.plot(rev)
print()

rev=[18000,25000,20000,45000,32000]
rev = np.sqrt(rev)
plt.plot(rev)
print()
