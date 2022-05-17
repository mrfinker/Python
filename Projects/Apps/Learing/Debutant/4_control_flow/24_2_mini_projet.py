"""
Vous créez un système de billetterie.
Le prix d'un billet simple est de 100 $.
Pour les enfants de moins de 3 ans, le billet est gratuit.

Votre programme doit prendre l'âge de 5 passagers comme entrée et sortir le prix total de leurs billets.

Exemple d'entrée
18
24
2
5
42

Exemple de sortie
400
Il y a un enfant de moins de 3 ans parmi les passagers, donc le prix total de 5 billets est de 400 $
"""

total=0
x=0
while x<5:
    age = int(input())
    if age>3:
        total += 100
    x+=1
print(total)

# Un autre programme similaire

"""
Un exemple de cas d'utilisation de continue:
Un système de billetterie aérienne doit calculer le coût total de tous les billets achetés.
Les billets pour les enfants de moins de 3 ans sont gratuits.
Nous pouvons utiliser une boucle while pour parcourir la liste des passagers et calculer le coût total de leurs billets.
Ici, l'instruction continue peut être utilisée pour ignorer les enfants.
"""

i = 0
nombre = int(input("Entrer le nombre de personne : "))

billet_enfant = 1.5
billet_ado = 5.5
billet_adulte = 15.5
total_vente = 0

while i < nombre:
    i += 1
    age = int(input("Entrer l'age : "))
    if age < 3:
        continue
    elif age >= 3 and age <= 12:
        total_vente += billet_enfant
    elif age >= 13 and age <= 17:
        total_vente += billet_ado
    elif age >= 18:
        total_vente += billet_adulte
print("Pour un nombre total de " , nombre , " personnes cela donne un total a payer de " , total_vente , " $")
print()