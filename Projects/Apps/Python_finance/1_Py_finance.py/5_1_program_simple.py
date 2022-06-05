try:
    import numpy_financial as npf
    res = npf.fv(rate = 0.08, nper = 5, pmt = 0, pv = -1000)
    print(res)
except ModuleNotFoundError:
    print("Nous avons trouver une erreur quelque part !")
print()


try:
    import numpy_financial as npf
    res = npf.fv(rate = 0.03, nper = 2, pmt = 0, pv = -500)
    print(res)
except ModuleNotFoundError:
    print("Nous avons trouver une erreur quelque part !")