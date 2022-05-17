"""
pour les boucles

Les boucles for vous permettent de parcourir facilement les listes.

Étant donné une liste de nombres, calculez leur somme à l'aide d'une boucle for.
Sortie de la somme après la boucle.
"""

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

somme = 0

for i in x:
    somme += i
print(somme)