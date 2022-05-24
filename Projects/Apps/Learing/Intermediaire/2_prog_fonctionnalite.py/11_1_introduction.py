"""
La programmation fonctionnelle est un style de programmation basé sur les fonctions
une partie clé de la programmation fonctionnelle est des fonctions d'ordre superieur
Les fonctions d'ordres superieur prennent d'autres fonctions comme arguments ou les retournent comme resultats
"""

def app_d(func, arg):
    return func(func(arg))

def ajouter_cinq(x):
    return x+5

print(app_d(ajouter_cinq, 10))
print()



def test(func, arg):
    return func(func(arg))

def mult(x):
    return x*x

print(test(mult, 2))
print()

"""
La programmation fonctionnelle cherche à utiliser des fonctions pures, qui n'ont aucun effet secondaire et ne retourent une valeur qui ne depends que de leurs arguments
La fonction pure :
"""

def pure_fonction(x, y):
    temp = x + 2*y
    return temp / (2*x + y)
print()

#La fonction impure

list = []
def impure(arg):
    list.append(arg)
print()
#Cette fonction est impure car elle change l'etat de "list"

def func(x):
    y = x**2
    z = x+y
    return z

"""
L'utilisation des fonctions pures a des avantages et des desavantages:
    ils sont plus facile a tester et plus efficaces
    une fois que la fonction a été evaluée pour une entree, le resultat peut etre stocké et referé la prochaine fois que la fonction de cette entree est necessaire
    reduisant le nombre de fois ou la fonction est appelée, c'est ce qu'on appelle la memorisation
    et est plus facile a executer en parallele

Les fonctions pures sont plus difficiles à ecrire dans certaines situation
"""