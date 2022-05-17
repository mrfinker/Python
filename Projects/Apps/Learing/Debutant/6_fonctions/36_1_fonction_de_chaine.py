"""
Formatage de chaîne

Les chaînes ont une fonction format(), qui permet d'y intégrer des valeurs, à l'aide d'espaces réservés.

Exemple:
Chaque argument de la fonction de format est placé dans la chaîne à la position correspondante, qui est déterminée à l'aide des accolades { }.
"""
nombres = [4, 5, 6]
msg = "Numéros: {0} {1} {2}". format(nombres[0], nombres[1], nombres[2])
print(msg)
print()

print("{0}{1}{0}".format("abra","cad"))
print()

"""
Vous pouvez également nommer les espaces réservés, au lieu des numéros d'index.
"""

a = "{x}, {y}".format(x = 5, y = 12)
print(a)
print()

str = "{c}, {b}, {a}".format(a = 5, b = 9, c = 7)
print(str)
print()

"""
join() joint une liste de chaînes avec une autre chaîne comme séparateur.
le resultat d'un Join() est un String
"""
x = ", ".join(["spam", "eggs", "ham"])
print(x)
print()

"""
split() est l'opposé de join(). Il transforme une chaîne avec un certain séparateur en une liste.
Nous avons utilisé un espace ' ' comme séparateur pour obtenir tous les mots de la chaîne sous forme de liste.
Par exemple, divisons une phrase en mots:
"""
str = "un texte va ici"
x = str.split(' ')
x.append(" ")
print(x)
print()

mot = str.split(" ")
res = mot[1]
print(res)
print()

"""
replace() remplace une sous-chaîne d'une chaîne par une autre.
"""

x = "Salut toi"
print(x.replace("toi", "vous"))
print()

x = str.replace("!", ".")

"""
lower() et upper() changent la casse d'une chaîne en minuscules et majuscules.
"""

print("Ceci est une lettre".upper())
print("Ceci est une lettre".lower())
print()

a = "Likofi"
b = a.upper()
print(b)
print()

txt = "bonjour"
print(max(txt))