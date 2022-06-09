import matplotlib.pyplot as plt

rev = [18000, 25000, 45000, 19500]
plt.plot(rev)
plt.savefig('plot.png')
print()


x = [2,8,42,1]
plt.plot(x)
print()


rev = [18000, 25000, 45000, 19500, 32000]
mois = ["juin", "juillet", "aout", "septembre", "octobre"]
plt.plot(mois, rev)
print()