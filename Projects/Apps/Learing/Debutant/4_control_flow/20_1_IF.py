## Condition avec IF
# pour verifier les conditions a executer durant le programme
# Python utilise l'indentation(espace vide au debut d'une ligne) pour delimiter les blocs de code

x = 42
if x > 5:
    print(x, "est superieur a 5") #ici x est toujours entier
    print(str(x) + " est superieur a 5") #ici x est devenus string pour le concatener !!!
print()

# Quel sera la sortie du code

pain = 8
if pain > 5:
    print("Cinq")
if pain > 9:
    print("Neuf")
print()

#----------------------------------------------------------------------------------------------

age = 15
if age > 18:
    print("deja Majeur")
print()

m = 12
n = 25
if m > n:
    print(m, " est superieur a ", n)
else:
    print(n, " est superieur a ", m)
print()

#parfois nous devrons effectuer des conditions tres complexes en imbriquant les conditions l'une sur l'autre

num = 12
if num > 5:
    print(num, " est superieur a 5")
    if num <= 17:
        print(num, " est entre 5 et 27")
print()

# l'indentation est utiliser pour definir le niveau de nidification

tax = 7
if tax > 3:
    print("3")
    if tax < 5:
        print("5")
        if tax == 7:
            print("7")