"""
Lecture de fichiers

Vous devez créer un programme pour lire le nombre donné de caractères d'un fichier.
Prenez un nombre N en entrée et sortez les N premiers caractères du fichier books.txt.
Le code donné ouvre le fichier books.txt. Utilisez l'objet file pour lire le contenu du fichier.
"""

file = open("/usercode/files/books.txt")
#your code goes here
n = int(input())
l = file.read()

print(l[:n])
file.close