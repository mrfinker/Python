class Animal:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur

class Chat(Animal):
    def miole(self):
        print("miaooouh")

class Chien(Animal):
    def aboie(self):
        print("whoouuuf")

fido = Chien("fido", "noire")
print(fido.couleur)
fido.aboie()
print()

class Loup:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur

    def bark(self):
        print("Grrr.....")

class Chien(Loup):
    def bark(self):
        print("whooouuuuh")

husky = Chien("Max", "Noire")
muxy = Loup("muxy", "Rouge")
husky.bark()
muxy.bark()
print()

class A:
    def method(self):
        print(1)

class B(A):
    def method(self):
        print(2)

B().method()
print()

class A:
    def mail(self):
        print(1)

class B(A):
    def mail(self):
        print(2)
        super().mail()

B().mail()