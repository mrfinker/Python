"""
Tuples


Vous recevez une liste de contacts, où chaque contact est représenté par un tuple, avec le nom et l'âge du contact.
Complétez le programme pour obtenir une chaîne en entrée, recherchez le nom dans la liste des contacts et affichez l'âge du contact dans le format présenté ci-dessous&nbsp;:

Exemple d'entrée
John

Exemple de sortie
Jean a 31 ans
Si le contact n'est pas trouvé, le programme doit afficher "Non trouvé".
"""
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

nom = input()
for i in contacts:
    if nom in i:
        print(str(i[0]) + " a "+ str(i[1]))
        break
else:
    print("Not found")
