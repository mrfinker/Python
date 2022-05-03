## Concatenation
# nous permet de melanger deux valeurs de type differents
# generalement des int et float, mais aussi avec des chaines ou String

print("Sam" + 'Rogers')
print()

# des chaines contenants des entiers sont considerer comme des chaines

print("5" + "8")
print()

# N'essayez pas d'ajouter une chaine à un nombre
# ce sont des valeurs de type differents donc cela donnera une erreur de TypeErrot print( 2 + "5" )

# on peut multiplier les chaines de carateres pour les affichers plusieurs fois ( donc les repeters )

print("Caleb" * 2)
print(3 * 'King')
print(3 * '7')
print(("A" + "B") * (1 + 2))
print()

# Ne pas essayer de multiplier une chaine par une chaine
# cela donnera une erreur TypeError : print("king" * "king")
# La meme chose si vous essayer de multiplier par un float print("king" * 2.5)

