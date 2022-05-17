"""
Fonctions de liste

Python a un tas de fonctions intégrées utiles pour les listes.
len() vous permet d'obtenir le nombre d'éléments dans une liste. Comme ça:
Contrairement aux éléments d'indexation, len ne commence pas par 0. La liste ci-dessus contient 5 éléments, ce qui signifie que len renverra 5.
"""

nombres = [1, 3, 5, 2, 4]
print(len(nombres))
print()

lettres = ["a", "b", "c"]
lettres += ["d"]
print(len(lettres))
print()

"""
Vous pouvez également utiliser len sur les chaînes pour renvoyer leur longueur (nombre de caractères).
Rappelez-vous que l'espace est aussi un caractère.
Par example:
"""

str = "un peu de texte"
x = len(str)
print(x)
print()

x = "abc"
x *= 2
print(len(x))
print()

"""
La fonction append() est utilisée pour ajouter un élément à la fin de la liste :
Notez que la fonction est appelée en utilisant le nom de la liste, suivi d'un point.
"""
nombres = [1, 2, 3]
nombres.append(4)
print(nombres)
print()

"""
insert() insère un nouvel élément à la position donnée dans la liste:
Le premier argument est l'index de position, tandis que le second paramètre est l'élément à insérer à cette position.
"""
mots = ["Python", "amusant"]
mots.insert(1, "est")
print(mots)
print()

num = [9, 8, 7, 6, 5]
num.append(4)
num.insert(2, 1)
print(len(num))
print()

"""
index() trouve la première occurrence d'un élément de liste et renvoie son index.
Une erreur est renvoyée si l'élément spécifié n'est pas trouvé dans la liste.
"""
lettres = ['p', 'q', 'r', 's', 'p', 'u']
print(lettres.index('r'))
print(lettres.index('p'))
print(lettres.index('q'))
print()

x = [2, 4, 5, 7, 4]
y = x.index(4)
print(y)
print()

"""
max(liste): renvoie la valeur maximale.
min(liste): renvoie la valeur minimale.
"""
x = [1, 8, 42, 3]
print(min(x))
print(max(x))
print()

num = [1, 3, 5, 2, 4]
res = min(num) + max(num)
print(res)
print()

"""
list.count(item): renvoie le nombre de fois qu'un élément apparaît dans une liste.
list.remove(item): supprime un élément d'une liste.
list.reverse(): inverse les éléments d'une liste.
"""

x = list(range(2, 10, 2))
print(x)
x.append(2)
x.append(15)
print(x.count(2))
x.remove(4)
print(x)
x.reverse()
print(x)
print()

list = [8, 4, 2, 6]
list.remove(2)
print(len(list) + list.count(6))
print()

num = [2, 4, 8, 9, 5]
num.insert(1, 3)
num.remove(9)
num.insert(0, num.count(8))
print(num[3])
print()