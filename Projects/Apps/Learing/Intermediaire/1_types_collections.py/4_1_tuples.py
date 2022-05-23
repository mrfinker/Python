"""
Tuples


Les tuples sont très similaires aux listes, sauf qu'ils sont immuables (ils ne peuvent pas être modifiés).
De plus, ils sont créés à l'aide de parenthèses plutôt que de crochets.
"""

mots = ("caleb", "roger", "pain")

"""
Vous pouvez accéder aux valeurs du tuple avec leur index, comme vous l'avez fait avec les listes:
"""

print(mots[0])

"""
Essayer de réaffecter une valeur dans un tuple provoque une erreur.
"""

#mots[1] = "jodiane"

"""
Comme les listes et les dictionnaires, les tuples peuvent être imbriqués les uns dans les autres.
"""

"""
Les tuples peuvent être créés sans les parenthèses en séparant simplement les valeurs par des virgules.

Les tuples sont plus rapides que les listes, mais ils ne peuvent pas être modifiés.
Exemple:
"""
mon_tuple = "un", "deux", "trois"
print(mon_tuple[0])