#Classe Methode
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calcule_aire(self):
        return self.largeur * self.hauteur

    @classmethod
    def nouvelle_carrer(cls, longueur_coter):
        return cls(longueur_coter, longueur_coter)

carrer = Rectangle.nouvelle_carrer(5)
print(carrer.calcule_aire())
print()

#Statique Methode
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validation_topping(topping):
        if topping == "Pomme":
            raise ValueError("Pas de pomme !")
        else:
            return True

Ingredients = ["piment", "oignon", "oeuf"]
if all(Pizza.validation_topping(i) for i in Ingredients):
    pizza = Pizza(Ingredients)
print()
