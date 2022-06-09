"""
Continuons avec notre projet Bitcoin !

Vous décidez de démarrer une entreprise minière Bitcoin en janvier 2017.
Vous faites un investissement initial de 500 000 $ pour acheter le matériel minier requis.
Chaque année, le matériel peut extraire 10 bitcoins, donc votre premier retour aura lieu le 1er janvier 2018.

Tâche
Calculez le rendement pour chaque année et affichez le TRI du projet.

Indice
Créez un tableau avec l'investissement initial comme premier élément (avec une valeur négative), suivi du coût de 10 bitcoins par an -- multipliez les valeurs du tableau donné par 10 et ajoutez-les en conséquence à la liste que vous avez créée, en les plaçant après la valeur d'investissement.
"""

import numpy as np
import numpy_financial as npf

#price for 2018-2021
bitcoin = [-500000, 3869.47*10, 7188.46*10, 22203.31*10, 29391.78*10]

res = npf.irr(bitcoin)
print(res)