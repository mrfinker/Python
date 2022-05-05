# Calculateur de pourboire
# Lorsque vous sortez manger, vous donnez toujours un pourboire de 20 % du montant de la facture.
# Mais qui a le temps de calculer le bon montant de pourboire à chaque fois ? Pas toi c'est sûr !
# Vous créez un programme pour calculer les pourboires et gagner du temps.

# Votre programme doit prendre le montant de la facture en entrée et en sortir le pourboire en flottant.

# Exemple d'entrée 50

# Exemple de sortie 10.0

# Explication : 20 % de 50 font 10.
# Pour calculer 20 % d'un montant donné, vous pouvez multiplier le nombre par 20 et le diviser par 100 : 50*20/100 = 10,0

bill = int(input())
#your code goes here
montant_p = 20
pourcent = 100
pourboire = float((bill * montant_p) / pourcent)

print(pourboire)