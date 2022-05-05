# la fonction input() renvoie une chaine de caractere
# pour le convertir en entier  c'est simple, nous utiliserons la fonction --- int(inut())
# type() permet de donner le type de la variable

age = int(input())
print(type(age))
print(age)
print()

age_1 = input()
print(type(age_1))
int(age_1)
print(type(int(age_1)))
print()

#----------------------------------------------------------------------------

x = "2"
y = "6"
z = int(x) + int(y)
print(z)
print()

# La meme chose pour le float, pour convertir une chaine en float

taille = float(input())
print(taille)
print(type(taille))
print()

x_1 = 9.45
y_1 = int(x_1)
print(y_1)
print()

# la fonction str() permet de convertir un numero en chaine
# on concatene le meme type comme appris precedemment

agge = 14
print("ceci est votre age " + str(agge))
print()

a = 5
b = 6
c = str(a)
d = str(b)
print(c + d)
print()

# et aussi on peut utiliser des input() autant de fois dans le programme
# juste ne pas en abuser

nom_game = input()
age_game = input()
print(nom_game + " a " + age_game)
print()