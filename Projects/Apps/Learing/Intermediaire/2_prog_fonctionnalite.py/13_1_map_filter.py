"""
map : le map et le filtre sont des fonctions integrees et fonctions de commande superieur tres utiles qui fonctionnent sur des listes(ou des objets similaires appelés iterable)
Le map de fonction prend une fonction et un iterable comme arguments et renvoie un nouveau iterable avec la fonction appliquée a chaque argument
"""

def ajout_cinq(x):
    return x+5

nums = [11,22,33,44,55]
res = list(map(ajout_cinq, nums))
print(res)
print()

# nous aurions pus avoir le meme resultat facilement en utilisant lambda
# pour convertir le resultat en liste, nous utilisons list()

nums = [11,22,33,44,55]
res = list(map(lambda x: x+5, nums))
print(res)
print()

nums = [11,22,33]
a = list(map(lambda x: x*2, nums))
print()

"""
Le filtre(filter), filtre les iterables en passant par chaque items qui correspond a la condition(autrement apppeler predicate ou predicat)
"""

nums = [11,22,33,44,55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
print()

# comme le map, le resultat serait convertit en liste si on veut l'afficher
# si nous mettons map a la place de filter, nous voyons qu'il est representer en Boolean

nums = [11,22,33,44,55]
res = list(map(lambda x: x%2==0, nums))
print(res)
print()