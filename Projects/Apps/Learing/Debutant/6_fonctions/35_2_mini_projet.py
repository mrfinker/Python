"""
Fonctions de liste

Vous travaillez sur un programme de gestion de file d'attente.
La file d'attente est représentée par une liste.
Écrivez un programme pour prendre une entrée, l'ajouter à la fin de la file d'attente et afficher la liste résultante.
La méthode append() peut être utilisée pour ajouter de nouveaux éléments à la liste
"""

queue = ['John', 'Amy', 'Bob', 'Adam']
x = str(input())
queue.append(x)
print(queue)