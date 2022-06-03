"""
Écriture de fichiers


Prenez un nombre N en entrée et écrivez les nombres 1 à N dans le fichier "numbers.txt", chaque nombre sur une ligne séparée.

Exemple d'entrée
4

Exemple de sortie
1
2
3
4

Le code donné lit le contenu du fichier et le sort.
Vous pouvez utiliser \n pour faire des sauts de ligne.
N'oubliez pas de fermer le fichier après y avoir écrit.
"""

n = int(input())

file = open("numbers.txt", "w+")
#your code goes here

for i in range(1, n+1):
    file.write(str(i)+"")
file.close()

f = open("numbers.txt", "r")
print(f.read())
f.close()