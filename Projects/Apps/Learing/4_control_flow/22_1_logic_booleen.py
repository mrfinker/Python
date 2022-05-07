"""
Il est maintenant temps de mettre à niveau nos booléens avec certains opérateurs,
qui nous permettent de combiner plusieurs conditions.
Commençons par l'opérateur and. C'est True, si les deux conditions sont évaluées à True :
Cours de Logic Mathematique
"""

print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(2 < 1 and 3 > 6)
print()

if (1 == 1) and (2 + 2 > 3):
    print("Vrai")
else:
    print("Faux")
print()

"""
Passons maintenant à l'opérateur ou.
L'opérateur ou est vrai si l'une (ou les deux) de ses conditions est vraie et faux si les deux conditions sont fausses
"""

print(1 == 1 or 2 == 2)
print(1 == 1 or 2 == 3)
print(1 != 1 or 2 == 2)
print(2 < 1 or 3 > 6)
print()

age = 15
argent = 500
if age > 18 or argent > 500:
    print("Bienvenue")
print()

"""
Comme vous pouvez le voir, en plus des valeurs,
vous pouvez également comparer des variables à des conditions de formulaire:
"""

mon_age = 25
limite = 18
taille = 176
if (mon_age > limite and taille > 180):
    print("Eligible")
else:
    print("Non eligible")
print()

heure = 16
jour = "Samedi"
if (heure > 20 or jour == "Dimanche"):
    print("Fermer")
else:
    print("ouvert")
print()

"""
Enfin, l'opérateur not fonctionne un peu différemment. not prend un seul argument et l'inverse.
Le résultat de not True est False, et not False devient True. Comme ça:
"""

print(not 1 == 1)
print(not 1 > 7)
print()

if not True:
    print("1")
elif not(1 + 1 == 3):
    print("2") # La reponse est 2
else:
    print("3")
print()

"""
Vous pouvez enchaîner plusieurs instructions conditionnelles dans une instruction if à l'aide des opérateurs booléens.
"""

Pays = "DRC"
age_client = 25
if (Pays == "DRC" or Pays == "US") and (age_client > 0 and age_client < 100):
    print("Original african congolese")
else:
    print("D'origine tout simplement")
print()

d_heure = 9
d_jour = 23
print(d_heure > 12 and d_jour <= 15) or (d_heure < 10)
print()

"""
L'ordre des opérations de Python est le même que celui des mathématiques normales:
les parenthèses d'abord, puis l'exponentiation, puis la multiplication/division, puis l'addition/soustraction.
"""

print(1 + 1 * 3)