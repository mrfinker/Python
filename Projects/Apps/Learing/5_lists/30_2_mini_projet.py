"""
Ranges

Vous créez un sélecteur de date pour un site Web et devez afficher toutes les années d'une période donnée.
Écrivez un programme qui prend deux nombres entiers en entrée et affiche la plage de nombres entre les deux entrées sous forme de liste.
La séquence de sortie doit commencer par le premier numéro d'entrée et se terminer par le deuxième numéro d'entrée, sans l'inclure.

Exemple d'entrée
2005
2011

Exemple de sortie
[2005, 2006, 2007, 2008, 2009, 2010]
Convertissez un objet de plage en liste et affichez-le.
"""

a = int(input())
b = int(input())

x = list(range(a, b, 1))

print (x)