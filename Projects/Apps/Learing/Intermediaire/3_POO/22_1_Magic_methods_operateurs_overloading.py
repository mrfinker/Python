import random

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, autre):
        return Vector2D(self.x + autre.x, self.y + autre.y)

premier = Vector2D(5, 7)
deuxieme = Vector2D(3, 9)
resulte = premier + deuxieme
print(resulte.x)
print(resulte.y)
print()

class SpecialMethod:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, autre):
        ligne = "=" * len(autre.cont)
        return "\n".join([self.cont, ligne, autre.cont])

pom = SpecialMethod("pom")
bonjour = SpecialMethod("Bonjour a tous !")
print(pom / bonjour)
print()


class specialMethod_2:
    def __init__(self, cont):
        self.cont = cont
    def __gt__(self, autre):
        for index in range(len(autre.cont)+1):
            result = autre.cont[:index] + ">" + self.cont
            result += ">" + autre.cont[index:]
            print(result)

pom = specialMethod_2("pomme")
viande = specialMethod_2("Viande")
pom > viande
print()

class ListeVague:
    def __init__(self, cont):
        self.cont = cont
    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]
    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = ListeVague(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
print()

