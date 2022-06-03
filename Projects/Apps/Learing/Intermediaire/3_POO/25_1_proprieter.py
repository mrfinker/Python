class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pommer_allouer(self):
        return False

pizza = Pizza(["pain", "tomate"])
print(pizza.pommer_allouer)
#pizza.pommer_allouer = True
print()

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pomme_allouer = False

    @property
    def pomme_allouer(self):
        return self._pomme_allouer

    @pomme_allouer.setter
    def pomme_allouer(self, valeur):
        if valeur:
            mot_de_passe = input("Entrer le mot de passe : ")
            if mot_de_passe == "motdepasse":
                self._pomme_allouer = valeur
            else:
                raise ValueError("Attention !!! infiltration !!!")
pizza = Pizza(["fromage", "tomate"])
print(pizza.pomme_allouer)
pizza.pomme_allouer = True
print(pizza.pomme_allouer)
