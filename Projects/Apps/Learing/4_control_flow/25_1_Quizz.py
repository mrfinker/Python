# Qu'est-ce que cela donnera

while False:
    print("Boucles")
print()

while True:
    x = input() # Casse la boucle si l'utilisateur entre la valeur 0
    if x == "0":
        break
print()

grade = int(input())
if grade > 70:
    print("Passe de promotion")
print()

i = 0
x = 0
while i < 4:
    x += i
    i += 1
print(x) # On s'arrete a 4
print()

x = int(input())
if x > 5:
    if x < 8:
        print(x + 1)
    else:
        print(x - 1)
else:
    print(x)
print()