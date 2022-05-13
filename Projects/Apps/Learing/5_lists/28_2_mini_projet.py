"""
Opérations de liste
Étant donné une liste de nombres, affiche "bingo" s'il contient le nombre saisi.
N'affiche rien si le numéro n'est pas trouvé.
"""

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

num = int(input())

if num in x:
    print("bingo")
else:
    print()