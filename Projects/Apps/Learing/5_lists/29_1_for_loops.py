"""
nous avons deja appris sur le while, maintenant apprenons le for
for est utiliser pour faire des iterations des listes ou strings
il definit la varaible qui prends la valeur de l'item concerner de la liste dans l'iteration
"""

mot = ["bonjour", "monde", "oeuf", "pain"]
for mots in mot:
    print(mots + "!")
print()
#Pour les mots de la liste dont on affecte les valeurs dans : mots, corresponds aux items de la liste qui seront boucler
#les affichers puit rajouter !!!

lettre = ["a", "b", "c"]
for i in lettre:
    print(i)
print()

num =[4, 7, 8, 5]
for x in num:
    print(x * 2)
print()

"""
il est aussi utiliser pour les iterations des strings
"""

str = "teste de l'iteration"
count = 0 # s'incrementera a chaque fois nous trouverons la valeur string "t"
for x in str:   # x represente l'item selon la position de l'index
    if(x == "t"):
        count += 1
print(count)
print()

"""
de la meme maniere avec le while, on utilise aussi les break et continue
pour arreter ou sauter une iteration
"""

text = "tu tourne es tres beau"
for x in text:
    if x == "e":
        break
    print(x)
print()

liste = [2, 3, 4, 5, 6, 7]
for x in liste:
    if(x % 2 == 1 and x > 4): # Affichera 5 puisqu'il correspond aux conditions
        print(x)
        break
print()

"""
nous savons que le for et le while sont utiliser pour repeter une ligne de code plusieurs fois, devrions-nous chosir :
nosu utilisons le for lorsque le nombre d'iteration est connus

nous utiliserons le while, qui est utile dans les cas ou le nombre d'iterations n'est pas connus et depends du programme
tant que les deux feront la meme chose pour le meme resultat, le for sera plus utiliser avec un syntax court et mieux
"""

num = [1, 2, 3, 4]
res = 0
for x in num:
    if(x % 2 == 0): # on saute si la condition est respecter puis on rajoute la valeur x a l'item res
        continue
    else:
        res += x
print(res)
print()

