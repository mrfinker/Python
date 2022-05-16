def min(x, y):
    if x <= y:
        return x
    else:
        return y

def somme(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(somme(9))
print()

def numero(x):
    for i in range(x):
        print(i)
        return
numero(10)

def ma_fonc(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(ma_fonc(3)) # La reponse est 3