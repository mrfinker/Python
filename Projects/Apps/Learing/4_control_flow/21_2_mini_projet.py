"""
Ecrire un programme pour contrôler l'entrée d'un club.
Seules les personnes âgées de 18 ans ou plus sont autorisées à entrer dans le club.
Votre programme prend l'âge de la personne qui essaie d'entrer et affiche
"Autorisé" s'il est autorisé à entrer dans le club et "Désolé" s'il est plus jeune que l'âge autorisé.
"""

age = int(input("Entrez votre age : "))
age_accorder = 18

if age >= age_accorder :
    print("Autoriser")
elif age < age_accorder :
    print("Desoler")