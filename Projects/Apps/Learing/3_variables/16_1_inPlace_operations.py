### In-place operations permettent d'ecrire du code comme x = x + 3, plus court x += 3

x = 10
print(x)

x = x + 5
print(x)

x += 3
print(x)

x %= 2
print(x)
print()

# la meme chose pour les operations numeriques de base que nous avions vus avant
# (+, -, *, /, %, **, //)

y = 4
y *= 3
print(y)
y -= 2
print(y)
y /= 3
print(y)
y **= 5
print(y)
y //= 3
print(y)
y %= 3
print(y)
print()

# ils peuvent etre aussi utiliser pour concatener des chaines caractere

z = "Roger"
print(z)

z += " Mutoto"
print(z)
print()

a = "be"
a *= 2
print(a)
print()

# et depuis le debut des nos cours tous ce qu'on a appris peuvent etre utiliser ensemble pour faire un programme assez complexe
# exemple : un programme qui prends une valeur en (miles) et le met en kilometre

miles = int(input("Entrer la valeur a convertir : "))
km = miles * 1.60934
print(km)