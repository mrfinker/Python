"""
Jeu de tir


Vous créez un jeu de tir&nbsp;!
Le jeu a deux types d'ennemis, des extraterrestres et des monstres. Vous tirez sur les extraterrestres à l'aide de votre laser et sur les monstres à l'aide de votre arme.
Chaque coup diminue la vie des ennemis de 1.
Le code donné déclare une classe ennemie générique, ainsi que les classes Alien et Monster, avec leur nombre de vies correspondant.
Il définit également la méthode hit() pour la classe Enemy.

Vous devez faire ce qui suit pour terminer le programme&nbsp;:
1. Héritez les classes Alien et Monster de la classe Enemy.
2. Complétez la boucle while qui prend en continu l'arme de choix à partir de l'entrée de l'utilisateur et appelez la méthode hit() de l'objet correspondant.

Exemple d'entrée
laser
laser
pistolet
sortir

Exemple de sortie
Alien a 4 vies
Alien a 3 vies
Monstre a 2 vies
La boucle while s'arrête lorsque l'utilisateur saisit 'exit'.
"""

class Enemy:
    name = ""
    lives = 0
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.name + ' killed')
        else:
            print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
    def __init__(self):
        super().__init__('Monster', 3)

class Alien(Enemy):
    def __init__(self):
        super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input()
    if x == 'exit':
        break