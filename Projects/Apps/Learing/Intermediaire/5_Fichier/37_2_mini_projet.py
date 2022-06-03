"""
Travailler avec des fichiers


Vous recevez un fichier books.txt, qui comprend les titres de livres, chacun sur une ligne distincte.
Créez un programme pour afficher le nombre de mots que contient chaque titre, au format suivant&nbsp;:
Ligne 1&nbsp;: 3 mots
Ligne 2&nbsp;: 5 mots
...

Assurez-vous de faire correspondre le format mentionné ci-dessus dans la sortie.
Pour compter le nombre de mots dans une chaîne donnée, vous pouvez utiliser la fonction split() ou, alternativement, compter le nombre d'espaces (par exemple, si une chaîne contient 2 espaces, alors elle contient 3 mots).
"""

with open("/usercode/files/books.txt") as f:
    #your code goes here
    j = 1
    for line in f:
        print( "Line " + str(j) + ": " + str(len(line.split(" "))) + " words")
        j += 1