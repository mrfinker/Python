"""
Pythn nous permet de creer des fonctions a la volee, à condition qu'elles soient creees à l'aide de la syntaxe lambda
ceci est couramment utiliser lors du passage d'une fonction simple comme argument à une autre fonction
La fonction cree a l'aide de la syntexe lambda sont appelées : anonymes
"""

def ma_func(f, arg):
    return f(arg)

ma_func(lambda x: 2*x*x, 5)
print()

"""
Les fonctions lambdas ne sont pas aussi puissantes que les fonctions nommees
ils ne peuvent faire que des choses qui necessitent une seule expression - generalement equivalentes à une seule ligne de code
"""

#fonction
def polynome(x):
    return x**2 + 5*x + 4
print(polynome(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))