try:
    num_1 = 7
    num_2 = 0
    print (num_1/num_2)
    print("Calcule effectuer !")
except ZeroDivisionError:
    print("L'erreur est resolus")
    print("on peut faire la division par zero")
print()

try:
    print("7" + 4)
except TypeError:
    print('Ceci ne peut pas marcher car les types sont different')
print()

try:
    var = 10
    print(10/2)
except ZeroDivisionError:
    print("erreur")
print("Terminer")
print()

try:
    var = 10
    print(var/2)
    print(var + " bonjour")
except ZeroDivisionError:
    print("Erreur de la division par zero")
except (ValueError, TypeError):
    print("Erreur trouver sur les types ou les valeurs des donnees")
print()

try:
    m = 42
    print(m / 0)
    print("l'amour de la vie") #on saute parcequ'on ne trouve aucune erreur
except (ValueError, TypeError):
    print("ValueError ou TypeError trouver dans le code")
except ZeroDivisionError:
    print("Division par zero")
print()

try:
    mot = "pomme"
    print(m/0)
except:
    print("Nous avons trouver une erreur dans le code")