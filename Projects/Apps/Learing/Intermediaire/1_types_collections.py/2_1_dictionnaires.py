"""
Dictionnaires

Python fournit un certain nombre de types de collection intégrés pour stocker plusieurs valeurs.
Les listes sont l'un de ces types de collection, et elles vous permettent de stocker des valeurs indexées :
"""

x = ['salut', 'bonjour', 'bienvenue']
print(x[2])
print()

"""
Chaque élément d'une liste possède un index, qui est défini automatiquement.
Les dictionnaires sont un autre type de collection et vous permettent de mapper des clés arbitraires sur des valeurs.
Les dictionnaires peuvent être indexés de la même manière que les listes, en utilisant des crochets contenant des clés.
Chaque élément d'un dictionnaire est représenté par une paire clé:valeur.
Exemple:
"""

âges = {
    "Dave": 24,
    "Marie": 42,
    "Jean": 58
    }
print(âges["Dave"])
print(âges["Marie"])
print()

voiture = {
    "BMW" : "bleue",
    "Peugeot" : "Rouge"
}

"""
Seuls les objets immutables peuvent être utilisés comme clés de dictionnaires. Les objets immutables sont ceux qui ne peuvent pas être modifiés.
Jusqu'à présent, les seuls objets mutables que vous avez rencontrés sont les listes et les dictionnaires.
Étant donné que les listes sont modifiables, le code ci-dessous génère une erreur.
Cela signifie que vous pouvez utiliser des chaînes, des entiers, des booléens et tout autre type immutable comme clés de dictionnaire.
"""
bad_dict = {
    [1, 2, 3]: "un deux trois",
}