"""
Retourner

Nous devons calculer l'aire d'un rectangle donné.
Votre programme doit prendre la largeur et la longueur en entrée et en sortie l'aire du rectangle.

Complétez la fonction d'aire, qui prend la longueur et la largeur comme arguments, pour calculer et renvoyer l'aire.
Appelez ensuite la fonction pour les entrées données.

Exemple d'entrée 1
7
4

Exemple de sortie 1
28
Pour trouver l'aire d'un rectangle, multipliez la longueur par la largeur.
"""

def aire(x, y):
    ar_rec = x * y
    return ar_rec

w = int(input())
h = int(input())

print(aire(w, h))