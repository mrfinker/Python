"""
Les fonctions

Nous avons une fonction qui affiche "Bienvenue, utilisateur" comme on l'appelle. Nous voulons le rendre plus personnalisé, alors reconcevez la fonction donnée afin qu'elle prenne le nom de l'utilisateur en entrée et qu'elle produise le message de bienvenue avec.

Exemple d'entrée
Tommy

Exemple de sortie
Bienvenue, Tommy

N'oubliez pas d'indenter l'instruction dans la fonction.
"""

def welcome():
    x = str(input())
    print("Welcome,", x)

welcome()