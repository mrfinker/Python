"""
Les comprehnsions des listes sont un moyen utile de creer rapidement des listes dont le contenu obeit à une regle
ils sont inspirées par la notation set-builder en mathematique
"""
cube = [i**3 for i in range(5)]
print(cube)
print()

num = [i*2 for i in range(10)]
print(num)
print()

"""
On peut egalement contenir une declaration if pour faire appliquer une condition sur les valeurs de la liste
"""

pim = [i**2 for i in range(10) if i**2%2==0]
print(pim)
print()