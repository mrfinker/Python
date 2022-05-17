"""
Les listes sont utilisées pour stocker des éléments.
Nous pouvons créer une liste en utilisant des crochets avec des virgules séparant les éléments. Comme ça:
Dans cet exemple, la liste de mots contient trois éléments de chaîne : Bonjour, monde et !
"""

mots = ["Bonjour", "monde", "!"]
num = [4, 5, 8, 9]

"""
Si vous souhaitez accéder à un certain élément de la liste, vous pouvez le faire en utilisant son index entre crochets.
Dans notre exemple, cela ressemblerait à ceci:
L'index du premier élément de la liste est 0, au lieu de 1, comme on pouvait s'y attendre.
"""

print(mots[0])
print(mots[1])
print(mots[2])
print()

print(num[2])
print()

"""
Les listes peuvent contenir différents types de données, tels que des chaînes et des nombres. comme mis ci-haut
ou meme les deux au meme moment
"""

"""
Mais les listes ne servent pas seulement à faire du shopping!
Nous pouvons faire des trucs plutôt sympas avec eux en Python.
Par exemple, nous pouvons utiliser des listes imbriquées pour représenter des grilles 2D, telles que des matrices.
Par example:

Ceci est utile car une structure de type matrice peut vous permettre de stocker des données au format ligne-colonne,
comme dans les programmes de billetterie, qui doivent stocker les numéros de siège dans une matrice,
avec leurs lignes et numéros correspondants.
"""

m = [
    [1, 2, 3],
    [4, 5, 8]
    ]

print(m[0][2]) # Affichera 3
print()

"""
Pour accéder aux éléments d'une matrice, on précise la ligne et la colonne de l'item à l'aide de crochets :
le code ci-haut genere la troisieme element de la premiere colonne
"""

n = ["texte", 0, [1, 5, 8], 5.68]
print(n[2][2]) # Affichera 8
print()

"""
Les chaînes peuvent également être indexées comme des listes!
Indexer une chaîne revient à créer une liste contenant chaque caractère de la chaîne.
L'espace (" ") est également un symbole et possède un index.
La chaîne "Bonjour" peut être considérée comme une liste, où chaque caractère est un élément de la liste.
Le premier élément est «B», le deuxième élément est «o», et ainsi de suite.

Par example:
"""

str = "Bonjour a tous"
print(str[5])
print()

x = "Pyhton"
print(x[1] + x[4]) # La reponse sera : yo
print()