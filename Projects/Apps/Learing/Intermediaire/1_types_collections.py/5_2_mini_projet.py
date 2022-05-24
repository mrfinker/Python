"""
Déballage de tuple

Les tuples peuvent être utilisés pour générer plusieurs valeurs à partir d'une fonction.
Vous devez créer une fonction appelée calc(), qui prendra la longueur du côté d'un carré comme argument et renverra le périmètre et l'aire à l'aide d'un tuple.
Le périmètre est la somme de tous les côtés, tandis que l'aire est le carré de la longueur du côté.

Exemple d'entrée
3

Exemple de sortie
Périmètre : 12
Superficie: 9
Le code donné prend un nombre à partir de l'entrée de l'utilisateur, le transmet à la fonction calc() et utilise la décompression pour obtenir les valeurs renvoyées.
"""
x = int(input())

def calc(x):
    return(x*4, x*x)

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))