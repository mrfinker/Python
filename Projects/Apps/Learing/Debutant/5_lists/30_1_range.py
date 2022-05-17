"""
on peut creer une sequence de nombre facilement avec : range()
par defaut il debute par 0 et s'incremente de 1 jusqu'a la valeur precise
"""

nombre = range(10)
print(nombre)
print()

x = range(5) # il y aura un nombre de 5 elements
print(x)
print()

"""
en ordre d'affichage meme dans une liste, nous avons besoin de d'abord le convertir en liste en utilisant la fonction : list()
"""

nombre = list(range(15))
print(nombre)
print()

num = list(range(5))
print(num[4])
print()

"""
si range est appeler avec un argument, il produira un objet avec une valeur depuis 0 a l'argument
si il est appeler avec deux arguments, il produira une valeur depuis le premier argument jusqu'au dernier elements exclus donc -1
"""

num = list(range(3, 10))
print(num)
print()

print(range(20) == range(0, 20))
print()

"""
si nous avons un troisieme argument qui est d'une grande utiliter, il est appeler Step(pas)
il determine l'intervale de sequence a produire
"""

num =list(range(5, 21, 2))
print(num)
print()

num = list(range(3, 15, 3))
print(num)
print(num[2])
print()

"""
Nous pouvons rentrer en arriere en utilisant la soustraction a la troisieme position, l'idee reste la meme, le deuxieme element sera exclus
"""

x = list(range(7, 3, -1))
print(x)
print()

num = list(range(5, 10, 2))
print(num)
print()

"""
nous pouvons utiliser range dans le for, sans avoir besoin de le convertir en liste
il est communement connus pour repeter des lignes des codes plusieurs fois
"""

for i in range(5):
    print("Bonjour")
print()

for i in range(0, 20, 2):
    print(i)
print()

x = list(range(0, 99))
print(x[4])
print()