"""
Somme des nombres consécutifs

Personne n'aime les devoirs,
mais votre professeur de mathématiques vous a confié la tâche de trouver la somme des N premiers nombres.
Gagnez du temps en créant un programme pour faire le calcul pour vous !
Prenez un nombre N en entrée et sortez la somme de tous les nombres de 1 à N (y compris N).

Exemple d'entrée
100

Exemple de sortie
5050

Explication : La somme de tous les nombres de 1 à 100 est égale à 5050.
Vous pouvez itérer sur une plage et calculer la somme de tous les nombres de la plage.
N'oubliez pas que la plage (a, b) n'inclut pas b, vous devez donc utiliser b + 1 pour inclure b dans la plage.
"""

N = int(input())

som = 0

for i in range (N):
    if i < N:
        som += i

som += N

print(som)