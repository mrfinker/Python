class Chat:
    def __init__(self, couleur, pate):
        self.couleur = couleur
        self.pate = pate

felix = Chat("Ginger", 4)
ruben = Chat("couleur-chien", 4)
stumpy = Chat("Brun", 3)

print(felix.couleur)
print()

class Chien:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur

    def aboie(self):
        print("whoof")

fido = Chien("fido", "Brun")
popy = Chien("morty", "noire")
print(fido.nom)
fido.aboie()
print()

class Etudiant:
    def __init__(self, nom):
        self.nom = nom

    def DireBonjour(self):
        print("Bonjour de " + self.nom)

s_1 = Etudiant("Armin")
s_1.DireBonjour()
print()

class Etudiant:
    def __init__(self, nom):
        self.nom = nom

test = Etudiant("Bobby")
print()