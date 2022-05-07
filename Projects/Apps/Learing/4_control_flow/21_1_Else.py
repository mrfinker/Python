"""
L'instruction else peut être utilisée pour exécuter certaines instructions lorsque la condition de l'instruction if est fausse
"""

x = 4
if x == 5:
    print("Oui")
else:
    print("Non")
print()

if 1 + 1 == 2:
    if 2 * 2 == 8:
        print("IF")
    else:
        print("ELSE")
print()

"""
Comme pour les instructions if, le code à l'intérieur du bloc doit être indenté.
Le deux-points à la fin du mot-clé else est important, ne le laissez pas de côté.
"""

grade = 87
if (grade >= 75):
    print("Vous passez")
else:
    print("Vous avez echouer")
print()

"""
Chaque bloc de condition if ne peut avoir qu'une seule instruction else.
Donc, pour que nous puissions effectuer plusieurs vérifications, nous devons enchaîner les déclarations if et else.
Par exemple, le programme suivant vérifie et affiche la valeur de la variable num sous forme de texte:
L'indentation détermine à quelles instructions if/else appartiennent les blocs de code.
"""

num = 3
if num == 1:
    print("Un")
else:
    if num == 2:
        print("Deux")
    else:
        if num == 3:
            print("Trois")
        else:
            print("Quelques chose d'autre")
print()

m = 10
n = 20
if m > n:
    print("IF condition")
else:
    print("ELSE condition")
print()

"""
Trop d'instructions if/else rendent votre code long et difficile à lire.
La meilleure façon de résoudre ce problème est l'instruction elif
(abréviation de else if). C'est un raccourci à utiliser lors de l'enchaînement des instructions if et else,
ce qui rend le code plus court et plus facile à lire.
Le même exemple de la partie précédente peut être réécrit en utilisant des instructions elif:
"""

num_1 = 3
if num_1 == 1:
    print("Un")
elif num_1 == 2:
    print("Deux")
elif num_1 == 3:
    print("Trois")
else:
    print("Quelques chose d'autre")
print()

"""
Et comme vous pouvez le voir dans l'exemple précédent, une série d'instructions if elif peut avoir un bloc else final,
qui est appelé si aucune des expressions if ou elif n'est True .
"""

num_2 = 8
if num_2 == 1:
    print("Un")
elif num_2 == 2:
    print("Deux")
elif num_2 == 3:
    print("Trois")
else:
    print("Quelques chose d'autre")
print()

num_3 = 45
if (num_3 < 0):
    print("Negative")
elif (num_3 > 0):
    print("Positive")
else:
    print("Valeur nulle")
print()

num_4 = 10
num_5 = 20
if num_4 > num_5:
    print(num_4 + num_5)
else:
    print(num_5 - num_4)