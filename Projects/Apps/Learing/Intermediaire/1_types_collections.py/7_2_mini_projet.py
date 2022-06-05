"""
Liste des compréhensions


Étant donné un mot en entrée, génère une liste contenant uniquement les lettres du mot qui ne sont pas des voyelles.
Les voyelles sont a, e, i, o, u.

Exemple d'entrée
impressionnant

Exemple de sortie
['w', 's', 'm']
Utilisez une compréhension de liste pour créer la liste de lettres requise et la produire.
"""

word = input()
vowels = ["a","e","u","o","i"]
a = [i for i in word if i not in vowels]
print(a)