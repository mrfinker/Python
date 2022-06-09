"""
Traçage


Continuons avec nos calculs Bitcoin.
Vous décidez d'investir 1000$ dans Bitcoin en 2018, au prix du tableau déclaré : 3869,47$.

Tâches
1. Calculez la valeur de votre investissement à la fin de chaque année en utilisant les prix indiqués dans le code.
2. Dessinez un tableau pour montrer combien votre investissement de 1 000 $ change de valeur chaque année.

Indice
Tout d'abord, calculez combien de Bitcoins vous aurez au départ en divisant votre investissement par le coût du Bitcoin la première année (le premier élément du tableau donné). Multipliez ensuite le tableau entier des prix par ce nombre pour obtenir la valeur pour chaque année. Utilisez np.multiply(array, number) pour multiplier un tableau par un nombre.

N'oubliez pas d'importer le package matplotlib.pyplot sous le nom "plt" pour dessiner le graphique à l'aide de la fonction plt.plot().
Ajoutez la fonction plt.savefig() (en utilisant le nom du graphique comme argument) à la fin du code pour dessiner le graphique dans le CodePlayground.
"""

import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt


#price for 2018-2021
invest = 1000/(3869.47*10)
bitcoin = [invest, 3869.47*10, 7188.46*10, 22203.31*10, 29391.78*10]
plt.plot(np.multiply(bitcoin, invest))
plt.savefig("plot.png")