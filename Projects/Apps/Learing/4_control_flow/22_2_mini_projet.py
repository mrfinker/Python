"""
Ecrire un programme,
qui donne l'âge d'une personne comme entrée, sortez son groupe d'âge.
Voici les tranches d'âge que vous devez gérer:

Enfant : 0 à 11 ans
Ado : 12 à 17 ans
Adulte : 18 à 64 ans

Exemple d'entrée
42
Exemple de sortie
Adulte

N'oubliez pas que vous pouvez utiliser l'opérateur booléen et pour combiner des conditions.
"""

age = int(input("Entrer un age : "))

if age >= 0 and age <= 11 :
    print ("Enfant")
elif age >= 12 and age <= 17 :
    print ("Ado")
elif age >= 18 and age <= 64 :
    print ("Adulte")