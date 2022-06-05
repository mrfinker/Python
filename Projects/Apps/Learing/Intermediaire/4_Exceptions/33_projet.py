"""
Système d'inscription


Vous créez un formulaire d'inscription pour un site Web.
Le formulaire a un champ de nom, qui doit comporter plus de 3 caractères.
Tout nom comportant moins de 4 caractères est invalide.
Complétez le code pour prendre le nom en entrée et déclenchez une exception si le nom n'est pas valide, en affichant "Nom invalide". Sortie "Compte créé" si le nom est valide.

Exemple d'entrée
abc

Exemple de sortie
Nom incorrect
Utilisez les instructions try/raise/except.
"""

try:
    name = input()
    #your code goes here
    x = len(name)
    if x > 3:
        print("Account Created")
    else:
        raise NameError
except:
    print("Invalid Name")