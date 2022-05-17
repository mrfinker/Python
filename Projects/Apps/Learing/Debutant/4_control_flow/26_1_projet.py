"""
Calculateur d'IMC

Le suivi de votre IMC est un moyen utile de vérifier si vous maintenez un poids santé.
Il est calculé à partir du poids et de la taille d'une personne, en utilisant cette formule : poids / taille²

Le nombre obtenu indique l'une des catégories suivantes:
Insuffisance pondérale = moins de 18,5
Normal = supérieur ou égal à 18,5 et inférieur à 25
Surpoids = supérieur ou égal à 25 et inférieur à 30
Obésité = 30 ou plus

Rendons la découverte de votre IMC plus rapide et plus facile,
en créant un programme qui prend le poids et la taille d'une personne en entrée
et produit la catégorie d'IMC correspondante.

Exemple d'entrée
85
1.9

Exemple de sortie
Normal

Le poids est en kg, la taille est en mètres.

Notez que cette hauteur est un flotteur.
"""

poids = int(input())
taille = float(input())

IMC = poids/(taille * taille)

if IMC  < 18.5:
    print("Underweight")
elif IMC >= 18.5 and IMC < 25:
    print("Normal")
elif IMC >= 25 and IMC < 30:
    print("Overweight")
elif IMC > 30:
    print("Obesity")