"""
Fonctions de dictionnaire


Vous travaillez sur des données qui représentent le classement de la liberté économique par pays.
Chaque nom et rang de pays est stocké dans un dictionnaire, la clé étant le nom du pays.

Complétez le programme pour prendre le nom du pays en entrée et en sortie son rang de liberté économique correspondant.
Dans le cas où le nom de pays fourni n'est pas présent dans les données, la sortie "Non trouvé".
Rappelons la méthode get() d'un dictionnaire, qui permet de spécifier une valeur par défaut.
"""

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

name = input("mettez le nom du pays: ".capitalize())
print(data.get(name, "Non trouvé"))