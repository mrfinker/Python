"""
Arguments

Les fonctions peuvent prendre des arguments, qui peuvent être utilisés pour générer la sortie de la fonction.

Comme vous pouvez le voir dans l'exemple, l'argument est défini à l'intérieur des parenthèses et est nommé mot.
Par example:
"""
def exclamation(mot):
    print(mot + " !")

exclamation("Pain")
print()

def double(x):
    print(2 * x)

double(3)
print()

"""
Vous pouvez appeler la même fonction avec des arguments différents.

Les arguments sont utilisés pour transmettre des informations à la fonction.
Cela nous permet de réutiliser la logique de la fonction pour différentes valeurs.
"""
def exclamation(mot):
    print(mot + " !")
exclamation("Pain")
exclamation ("mayonnaise")
exclamation("python")
print()

def x(y):
    print(y + 2)

x(5)
print()

"""
Encore mieux, vous pouvez définir des fonctions avec plus d'un argument ; séparez-les par des virgules. Comme ça:
"""

def somme(x, y):
    print(x + y)
    print(x - y)

somme(5, 8)
print()

def multiple(x, y):
    print(x * y)

multiple(5, 8)
print()

"""
Comme vous pouvez le voir dans les exemples précédents, les arguments peuvent être utilisés comme variables à l'intérieur de la fonction.
Vous pouvez avoir différentes instructions dans vos fonctions, en travaillant avec les variables d'argument, telles que les instructions if et les boucles.
"""

def pair(x):
    if x % 2 == 0:
        print("Oui")
    else:
        print("Non")
pair(6)
print()

def msg(num, char):
    print(char + str(num))

msg(18, "A")
print()