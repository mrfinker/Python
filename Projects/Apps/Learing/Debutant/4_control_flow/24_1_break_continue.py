"""
    BREAK
Pour terminer prématurément une boucle while, nous pouvons utiliser une instruction break.
Par exemple, nous pouvons casser une boucle infinie si une condition est remplie:
"""

i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print("On arrete ici") # On va inclure 5 car il vient apres l'incrementation
        break
print("On a terminer")
print()

i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2: # Il va afficher 5,4,3
        break
print()

"""
Voici un exemple de cas d'utilisation de break:
Une boucle while infinie peut être utilisée pour prendre en continu l'entrée de l'utilisateur.
Par exemple, vous fabriquez une calculatrice et devez prendre des nombres de l'utilisateur pour les additionner
et vous arrêter lorsque l'utilisateur entre "stop".

Dans ce cas, l'instruction break peut être utilisée pour terminer la boucle infinie lorsque l'entrée utilisateur est égale à "stop".
L'utilisation de l'instruction break en dehors d'une boucle provoque une erreur.
"""

i = 0
while True:
    print(i)
    i = i + 1
    if i > 5: # comme 5 n'est pas superieur lui-meme il fera partis de la boucle
        break
print()

"""
Une autre instruction qui peut être utilisée dans les boucles est continue.
Contrairement à break, continue saute en haut de la boucle, plutôt que de l'arrêter.
Fondamentalement, l'instruction continue arrête l'itération en cours et continue avec la suivante.

on ne peut pas utiliser continue pour arreter une boucle infinie
"""

i = 0
while i < 5:
    i += 1
    if i == 3:
        print("On saute 3")
        continue
    print(i)
print()

i = 0
while True:
    i += 1
    if(i == 2):
        continue
    if(i == 5):
        break
    print(i) #1,3,4
print()