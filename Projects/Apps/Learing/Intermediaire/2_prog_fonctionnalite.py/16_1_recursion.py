# x = int(input("Entrer une valeur : "))

def factoriel(x):
    if x == 1:
        return 1
    else:
        return x * factoriel(x-1)

print(factoriel(5))
print()

def pairs(x):
    if x == 0:
        return True
    else:
        return  impairs(x-1)

def impairs(x):
    return not pairs(x)

print(impairs(17))
print(pairs(23))
print()

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(4))