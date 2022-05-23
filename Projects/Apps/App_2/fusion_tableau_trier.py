def fusionList(premier, second):
    combiner = premier + second
    combiner.sort()
    return combiner

groupe_1 = [11,13,18,17,56]
groupe_2 = [12,15,19,43,66]
fusionner = fusionList(groupe_1, groupe_2)
print(fusionner)