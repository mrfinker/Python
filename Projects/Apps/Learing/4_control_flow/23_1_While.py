"""
Les boucles permettent de répéter plusieurs fois un bloc de code.
Par exemple, disons que nous devons traiter plusieurs entrées utilisateur,
de sorte que chaque fois que l'utilisateur entre quelque chose, le même bloc de code doit être exécuté.
"""

"""
Voici une boucle while contenant une variable qui compte de 1 à 5, à quel point la boucle se termine.

Lors de chaque exécution de boucle, la variable i est incrémentée de un, jusqu'à ce qu'elle atteigne 5.
Ainsi, la boucle exécutera l'instruction print 5 fois.
"""

i = 1
while i <= 5:
    print(i)
    i = i + 1 # Si nous ne mettons pas il y aura une boucle infinie et il y aura 5 valeurs afficher
print("Terminer")
print()

"""
Les instructions à l'intérieur de la boucle while doivent être indentées, comme une instruction if.
"""

x = 0
while x < 10:
    print(x)
    x += 1
print("On a finis")
print()

x = 10
while x >= 0:
    print(x)
    x -= 1 # Si nous mettons ça x += 1 il y aura boucle infinie
print("On a finis")
print()

"""
Le code dans le corps d'une boucle while est exécuté à plusieurs reprises tant que la condition est vraie.
C'est ce qu'on appelle l'itération rapelle du cours de logique mde prgrammation.

Le code suivant ajoute le nombre actuel à la variable somme à chaque itération:
"""

somme = 0
x = 10
while x > 0:
    somme += x
    x -= x
print(somme) # La valeur de somme est 10, car x = x -x qui donne 0
print()

i = 3
while i >= 0:
    print(i) # Il y aura 4 valeurs afficher 3,2,1 et le zero
    i = i - 1
print()

"""
Vous pouvez également utiliser d'autres instructions, telles que des instructions if dans des boucles.
Ceci est particulièrement utile dans des jeux,
où vous devrez peut-être parcourir un certain nombre d'actions de joueurs et ajouter ou supprimer des points au score du joueur.
Découvrez ce code, qui utilise une instruction if/else dans une boucle while
pour séparer les nombres pairs et impairs dans la plage de 1 à 10:
"""

x = 1
while x < 10:
    if x % 2 == 0:
        print(str(x) + " est pair")
    else:
        print(str(x) + " est impair")
    x += 1
# x += 1 si nous le mettons ici il y aura une boucle car le x sera a l'exterieur de la boucle while donc pas d'incrementation
print()

x = 0
while x <= 20:
    print(x)
    x += 2
print()

"""
Si la condition de la boucle while reste True, la boucle s'exécutera indéfiniment, provoquant une boucle infinie.
Un moyen rapide de créer une boucle infinie consiste à utiliser while True.

Ces deux sont des boucles infinies
x = 8
while x > 3:
    print(x)

x = 1
while x == 1:
    print("Dans la boucle")

"""

x = 5
while x > 0:
    print(x)
    x -= 1