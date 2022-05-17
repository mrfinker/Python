"""
commentaires

Nous sommes si près de la ligne d'arrivée ! Bravo d'être arrivé jusqu'ici !
Les commentaires sont des annotations au code utilisées pour le rendre plus facile à comprendre. Ils n'affectent pas la façon dont le code est exécuté.
En Python, un commentaire est créé en insérant un octothorpe (autrement connu sous le nom de signe dièse ou symbole dièse : #). Tout le texte qui suit sur cette ligne est ignoré.
"""

x = 365
y = 7

print(x % y) # trouvons le reste
print()

x = 8
# affiche 8
print(x)
print()

"vous pouvez avoir plusieurs commentaires"

x = 365
y = 7
# ceci est un commentaire
print(x % y) # trouvons le reste
# print(x // y)
# un autre commentaire
print()

x = 5
#x += 1
x += 2 # incrementation
print(x)
print()

"""
Les docstrings (chaînes de documentation) sont similaires aux commentaires, en ce sens qu'ils sont conçus pour expliquer le code. Mais, ils sont plus spécifiques et ont une syntaxe différente.
Ils sont créés en plaçant une chaîne multiligne contenant une explication de la fonction sous la première ligne de la fonction. Comme ça:
"""

def malade(mot):
    """
    afficher le  mot avec une exclamation,
    de la maniere suivnte
    """
    print(mot + " ! ")
malade("pomme")
print()

"""
Les docstrings servent de documentation pour les autres développeurs qui utilisent votre fonction.
Contrairement aux commentaires conventionnels, les docstrings sont conservés tout au long de l'exécution du programme. Cela permet au programmeur d'inspecter ces commentaires au moment de l'exécution.
"""

