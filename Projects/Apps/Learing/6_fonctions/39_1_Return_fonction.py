"""
Retour des fonctions

Certaines fonctions, telles que int ou str, renvoient une valeur au lieu de l'afficher.
La valeur renvoyée peut être utilisée plus tard dans le code, par exemple, en étant affectée à une variable.

Pour ce faire pour vos fonctions définies, vous pouvez utiliser l'instruction return. Comme ça:
"""

def somme(x, y):
    return x + y

def carrer(x):
    return x**2

"""
Nous pouvons maintenant utiliser notre fonction et affecter le résultat à une variable:
Le retour est utile lorsque vous n'avez pas besoin d'afficher le résultat de la fonction, mais que vous devez l'utiliser dans votre code.
Par exemple, la fonction retrait() d'un compte bancaire pourrait renvoyer le solde restant du compte.
"""
def somme(x, y) :
    return x+y

res = somme(42, 7)
print(res)
print()

def peau(x, y):
    if x >= y:
        return x
    else:
        return y

x = peau(4, 7)
print(x)
print()

"""
Vous pouvez utiliser la valeur renvoyée dans votre code, par exemple, une instruction if:
"""

def max(x, y):
    if x >= y:
        return x
    else:
        return y

if(max(6, 4) >  10):
    print("Oui")
else:
    print("Non")
print()

def court_string(x, y):
    if len(x) <= len(y):
        return x
    else:
        return y
print()

"""
Une fois que vous renvoyez une valeur d'une fonction, elle cesse immédiatement d'être exécutée.
Tout code placé après l'instruction return ne sera pas exécuté.
"""
def addition(x, y):
    total = x + y
    return total
    print("Ceci ne sera pas afficher a cause de sa place")

print(addition(4, 5))
print()

def  nombre():
    print(1)
    print(2)
    return
    print(4)
    print(6)
print()

"""
Une fonction ne peut retourner qu'une seule fois, donc, si vous avez besoin de retourner plusieurs valeurs, vous pouvez utiliser une liste.
"""

def double_double(a, b):
    return[a*2, b*2]

x = double_double(6, 9)
print(x)
print()

def calcul(x, y):
    return[x + y, x * y]

res = calcul(3, 4)
print(res[1])
print()

def somme(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(somme(4))