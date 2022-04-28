#Ecrire un rpogramme python qui accepte le rayon d'un cercle de l'utilisateur et calcule l'aire
from math import pi

r = float(input("Mettez le radian du cercle : "))
print("L'aire du cercle avec le radian " + str(r) + " est: " + str(pi * r**2))