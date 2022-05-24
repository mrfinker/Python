"""
Déballage de tuple

Le déballage de tuple vous permet d'affecter chaque élément d'une collection à une variable.

Cela peut également être utilisé pour échanger des variables en faisant a, b = b, a , puisque b, a sur le côté droit forme le tuple (b, a) qui est ensuite décompressé.
Exemple:
"""
nombres = (1, 2, 3)
a, b, c = nombres
print(a)
print(b)
print(c)
print()

"""
Une variable précédée d'un astérisque (*) prend toutes les valeurs de la collection qui restent des autres variables.

Exemple:
c se verra attribuer les valeurs 3 à 8.
"""
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b)
print(c)
print(a)
print(d)
print()

a,b,c,d,*e,f,g = range(20)
print(len(e))
