"""
Ceci nous permet d'avoir une partie de la liste
nous utilisons deux colonnes separer par un indice, retournant une nouvelle liste
containant les elements de la liste selon les indices precis
de la meme maniere que le range(), le premier index est toujours 0 et inclus tandis que le second non
"""

nombre = list(range(15))
print(nombre)
print(nombre[2:6])
print(nombre[3:8])
print(nombre[0:1])
print(nombre[0:2])
print(nombre[4:7])
print()

"""
si la premiere valeur est omis, il prendra du debut jusqu'a la seconde valeur
"""

print(nombre[:7])
print(nombre[:5])
print(nombre[:10])
print()

"""
si la deuxieme valeur est omis, il prendra de la premiere valeur jusqu'a la fin
"""

print(nombre[7:])
print(nombre[5:])
print(nombre[9:])
print()

"""
comme le range(), si nous sommes en presence d'une troisieme valeur c'est une Step(pas)
"""

print(nombre[::]) # prends tout les elements du debut a la fin
print(nombre[::2])
print(nombre[::4])
print(nombre[2:8:3])
print()

test = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(test[1::4]) # on commence a 1, puis il devient a 0 pour compter 4 depuis 0, puis l'index suivant devient 0 ensuite nous compterons 4 depuis 0 ainsi de suite
print()

"""
la valeur negative peut aussi etre utiliser ici
il est utiliser pour le premier et deuxieme valeur, pour compter a partir de la fin de la liste
si la valeur negative est utiliser sur le Step nous aurons un comptage arriere
"""

print(nombre[1:-1])
print(nombre[7:5:-1])
print(nombre[5:1:-2])
print()

"""
[::-1], nous utiliserons ceci pour inverser la liste, ceci est plus utiliser et connus de tous
"""

num = nombre[::-1]
print(num)
print(num[2])
print()

nom = "Caleb"
print(nom[1:-1])
print()