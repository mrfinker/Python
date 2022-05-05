# Maintenant on peut utiliser les variables pour faire des operations

x = 7
print(x)

print( x + 5)
print(x)
print()

# Nous remarquons que la variable stocke sa valeur au long du programme

p = "Roger"
print( p * 3)
print()

# il est facile de changer la valeur d'une valeur, elles peuvent etre reaffecter autant de fois voulus

y = 125.25
print(y)

y = "Ceci est une chaine de caractere"
print(y + " !")
print()

### Faire attention repeter la meme variable plusieurs fois avec des types ded donnees differents
### n'est pas une bonne pratique a eviter

age = 12
age = 24 - 6
print(age)
print()

# un programme peut inclure plusieurs variables pouvant etre utiliser ensemble pour produire un resultat

a = 15
nom = "Caleb"

print(a * nom)
print()

w = 5
l = 7
print(w + l)
print()

# vous pouvez utiliser la declaration (del) pour supprimer une variable
# et essayer d'utiliser une variable supprimer provoque une erreur (NameError)

f = 14
print(f)
del f
print()

# ceci provequera une erreur comme elle vient apres sa suppression --- print(f)
# remarquons que avant d'etre supprimer l'affichage passe puisqu'elle vient avant sa suppression

pain = 2
boudin = 6
del pain

# ceci affichera une erreur --- print(pain * boudin)

# Les variables supprimer peuvent etre reaffecter
# reprenons notre exemple precedent

pain = 2
boudin = 6
del pain
pain = 5
print(pain * boudin)
print()

#-------------------------------------------------

ju = 2
cake = 3
del ju
cake = 8
ju = 5
print(cake * ju)