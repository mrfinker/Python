### Les booleens
# Les boolens ont deux valeurs soit vrai soit faux (True or False) en commençant par le majuscule
# Nous pouvons creer des booleens en comporant les valeurs en utilisant l'operateur (==)

mon_bool = True
print(mon_bool)
print(2 == 3)
print("hello" == "Hello") #False H et h sont deux lettre dans python
print()

# ne pas confondre le signe (=) pour l'affectation et (==) pour la comparaison

ouvert = True
fermer = False
print()

### comparaison
# les booleens sont cree lors de la comparaison des valeurs
# nous avons des operateurs de comparaison :
#  (==) egal à, (!=) pas egal à ou different de, (>) stritectement superieur à, (<) stritectement inferieur à
# (>=) superieur ou egal à --- surtout ne pas inverser l'ordre
# (<=) inferieur ou egal à

x = 7

print(x == 7)
print(x == 8)
print(x != 8)
print(x != 7)
print(x < 7)
print(x < 8)
print(x > 7)
print(x > 8)
print(x >= 7)
print(x >= 8)
print(x <= 7)
print(x <= 8)
print()

# Les operateurs de comparaison sont aussi appeler OPERATEURS RELATIONNELS
# < et >, peuvent aussi etre utiliser pour comparer les chaines lexicographiquement(ordre alphabetique des mots qui est basé sur l'ordre alphabetique de leurs lettre composants)

print("a" > "b")
print("b" > "a")
print("Bob" > "Dave")
print("Bob" > "Boc")
print("hey" < "hay")
print()

## Les valeurs vraies et fausses booleennes peuvent etre representer comme des entiers 1 et 0
# nous utiliserons la fonction int() pour convertir le booleen en entier

y = (4 == 7)
print(int(y))
z = (7 == 7)
print(int(z))