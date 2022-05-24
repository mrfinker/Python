def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print(factorial(4))

# ou encore

def factoriel(n):
    if n <= 1:
        return 1
    else:
        return n * factoriel(n-1) #recursivité car nous appelons la fonction dans la fonction

print(factoriel(4))