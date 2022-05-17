## Newlines
# Le Backslash permet de cree une nouvelle ligne dans le texte
# nous utilisons \n qui est identiques a print()
# mais la seule difference est que le second ne se place pas a l'interieur de la phrase

print("Un \n Deux \nTrois")
print()

## Tab
# Similaire a une nouvelle ligne, on peut creer un onglet ou Tab \t

print("\t Salut \t a tous")
print()

## Carriage Return
# Le symbole de retour du chariot \r
# On l'utilise pour deplacer le curseur au debut de la ligne
# Seul guillement est qu'il risque de ne pas marcher comme prevus dans tous les environnements

print("Salut \r a tous")
print()

## Escaping
# pour inclure les caracteres speciales dans un texte, par exemple :

print("Pour faire une nouvelle ligne nous utilisons \\n")
print("\\r\\n")
print()

## difference entre \n et \r
# il differe selon celui qui les utilisent
# windows utilise \r\n tandis que Unix et Lunix \n

print("\r\n\r\n\r\n") # on appuie 3 fois sur entrer
print()

## Newlines
# \n peut etre encombrant si nous voulons formater plusieurs texte multiligne
# et pour cela il y a une methode

print(""" Ceci
    est une
      nouvelle ligne
        pour plusieurs
            texte""")

# ceci facilite le formatage de longs textes multilignes sans avoir besoin de mettre plusieurs fois \n pour les sauts de ligne

print(''' Ceci
    est une
      nouvelle ligne
        pour plusieurs
            texte l'un comme l'autre ''')

# Sans avoir besoin de mettre encore \n dans le texte