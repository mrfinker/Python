"""
Moteur de recherche

Vous travaillez sur un moteur de recherche. Surveillez vos arrières Google!
Le code donné prend un texte et un mot en entrée et les transmet à une fonction appelée search().

La fonction search() doit retourner "Mot trouvé" si le mot est présent dans le texte, ou "Mot introuvable", s'il ne l'est pas.

Exemple d'entrée
"C'est génial"
"génial"

Exemple de sortie
Mot trouvé

Définissez la fonction search(), afin que le code donné fonctionne comme prévu.
"""

def search(x, y):
    if y in x:
        print("mot trouver")
    else:
        print("mot introuvable")

text = input()
word = input()

search(text, word)