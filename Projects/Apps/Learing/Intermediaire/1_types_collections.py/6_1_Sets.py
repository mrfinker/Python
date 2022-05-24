"""
Les ensembles ou Sets sont similaires aux listes ou aux dictionnaires, ils sont cree a l'aide de {} et ne sont pas commandés donc ils ne peuvent pas etre indexé
en raison de la façon dont ils sont stocker, il est plus rapide de verifier si un article fait partie d'un ensemble en utilisant l'operateur : in, plutot que d'une partie d'une liste
le Sets ne peuvent contenir des valeurs doubles
"""

num_set = {1,2,3,4,5}
print(3 in num_set)
print()

letters = {"a","b","c","d"}
if "e" not in letters:
    print(1)
else:
    print(2)
print()

"""
nous pouvons utiliser la fonction add() pour ajouter de nouveaux elements au Sets et
remove() pour supprimer un element specifique
les elements en double seront automatiquement supprimer du Sets
La fonction len() est utiliser pour renvoyer les nombres d'elements dans le Set
"""

nums = {1,2,1,3,1,4,5,6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
print()

"""
Le Sets peuvent etre combinés à l'aide d'operations mathematiques
L'union |, combine deux Sets pour former un nouveau contenant des elements de deux Sets
L'intersection &, obtient les elements identiques appartenant seulemnt aux deux Sets
La Difference -, obtient les elements dans le premier Sets mais pas dans le deuxieme
La Difference symetrique ^, obtient des elements dans l'un ou l'autre Sets mais pas les deux
"""

premier = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}

print(premier | second)
print(premier & second)
print(premier - second)
print(second - premier)
print(premier ^ second)
print()

a = {1,2,3}
b = {0,3,4,5}
print(a & b)
print()
