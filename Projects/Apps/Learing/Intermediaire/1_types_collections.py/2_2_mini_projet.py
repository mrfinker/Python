"""
Dictionnaires

Vous travaillez chez un concessionnaire automobile et stockez les données de la voiture dans un dictionnaire:
Votre programme doit prendre la clé en entrée et sortir la valeur correspondante.

Exemple d'entrée
annee

Exemple de sortie
2018
Les données sont déjà définies dans le code.
"""
voiture = { 'marque': 'BMW',
            'annee': 2018,
            'couleur': 'rouge',
            'mileage': 15000}

x = input()
print(voiture[x])