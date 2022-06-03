file = open("nouvelle_fichier_test.txt")
cont = file.read()
print(cont)
file.close()
print()


file = open("test.txt")
cont = file.read()
print(cont)
file.close()
print()


file = open("nouvelle_fichier_test.txt")
print(file.read(5))
print(file.read(7))
print(file.read())
file.close()
print()


file = open("nouvelle_fichier_test.txt")
for line in file.readlines():
    print(line)
file.close()
print()


file = open("nouvelle_fichier_test.txt")
for line in file:
    print(line)
file.close()
print()


file = open("test.txt", "r")
for i in range(21):
    print(file.read(4))
file.close()
print()


file = open("test.txt", "r")
cont = file.readlines()
print(cont[1])
file.close()
