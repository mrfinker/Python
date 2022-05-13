list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
print()

for i in range(10):
    if not i % 2 == 0: # affichera toutes les valeurs divisible par deux, depuis 2 jusuqu'a 10
        print(i + 1)
print()

list = (1, 2, 3)
for var in list:
    print(var)
print()

x = input()
print(x[0:3])
print()

x = [6, 4, 2, 9]
x = x[::-1]
print(x[0] + x[2])
print()