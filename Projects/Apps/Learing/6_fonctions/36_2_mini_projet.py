"""
Fonctions de chaîne

Votre ami vous a envoyé un message, mais son clavier est cassé et tape un # au lieu d'un espace.

Remplacez tous les caractères # dans l'entrée donnée par des espaces et affichez le résultat.
Vous pouvez utiliser la fonction replace() d'une chaîne pour remplacer une sous-chaîne par une autre.
"""

msg = input()

x = msg.replace("#", " ")
print(x)