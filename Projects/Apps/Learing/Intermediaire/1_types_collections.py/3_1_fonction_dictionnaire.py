"""
Pour déterminer si une clé se trouve dans un dictionnaire, vous pouvez utiliser in et not in,
comme vous pouvez le faire pour une liste.

Exemple:
"""
nombres = {
    1: "un",
    2: "deux",
    3: "trois",
}
print(1 in nombres)
print("trois" in nombres)
print(4 not in nombres)
print()

"""
Une fonction de dictionnaire utile est get.
Il fait la même chose que l'indexation, mais si la clé n'est pas trouvée dans le dictionnaire,
il renvoie une autre valeur spécifiée à la place.

Pour déterminer le nombre d'éléments d'un dictionnaire, utilisez la fonction len().
"""
pairs = {
    1: "apple",
    "orange": [2,3,4],
    True: False,
    12: "True",
}

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))
print()

fib = {
    1:1,
    2:1,
    3:2,
    4:3
}
print(fib.get(4,0) + fib.get(7,5))
print()