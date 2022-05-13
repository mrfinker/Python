"""
les items des certains index peuvent etre reassigner
"""

num = [5, 9, 8]
num[1] = 52
print(num) # [5, 52, 8]
print()

num = [1, 2, 3, 4, 5]
num[3] = num[1]
print(num[3])
print(num)
print()

"""
nous pouvons ajouter aussi ou concatener des lists comme des strings
"""

num = [1, 2, 3]
print(num)
print(num + [4, 5, 6])
print()

x = [2, 4]
x += [6, 8]
print(x[2] // x[0]) # La reponse est 3
print()

"""
les listes et les strings ont plusieurs similarités
les listes peuvents aussi etre multiplier par les entiers
"""

num = [1, 2, 3]
print(num * 3)
print()

x = [2, 4]
x = x * 3
print(x[3])
print()

"""
Pour verifier si un item est dans une liste particuliere, nous utilisrns l'operateur : in
il retourne vraie si l'item est repris une ou plusieurs fois dans liste et faux si il n'y est pas
"""

mot = ["pain", "fromage", "jus", "mayonnaise"]
print("jus" in mot)
print("coca" in mot)
print()

num = [10, 9, 8, 7, 6, 5]
num[0] = num[1] - 5
if 4 in num:
    print(num[3])
else:
    print(num[4])
print()

"""
l'operateur in est aussi utiliser pour determiner oui ou non un string est un ... dans un autre string
"""

x = "bonjour a tous"
if "monde" in x:
    print("Oui")
print()

text = input()
if("caleb" in text):
    print("Le big boss")
else:
    print("Tu ne sais pas ce que tu rates")
print()

"""
pour verifier si un item n'est pas dans une liste, on utilise l'operateur : not
"""

num = [1, 2, 3]
print(not 4 in num)
print(4 not in num)
print(not 3 in num)
print(3 not in num)
print()