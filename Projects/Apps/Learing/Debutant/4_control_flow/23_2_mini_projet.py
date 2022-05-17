"""
On vous donne un programme qui sort tous les nombres de 0 à 10.
Modifiez le code pour qu'il n'affiche que les nombres pairs.
Tout nombre entier qui peut être divisé exactement par 2 est un nombre pair.
"""

x = 0
while x <= 10:
    if x%2 == 0:
        print(x)
    x += 1
print()

# Autrement

x = 0
while x<=10:
    print(x)
    x+=2