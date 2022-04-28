#Ecrire un programme python qui accepete une sequence de numeros separés par des virgules de l'utilisateur
#et genere une liste et un tuple avec ces numeros

#Une liste est un conteneur qui detient des valeurs separees par virgule entre crochet ou les elements ne doivent pas tous avoir le meme type
#ces contenus peuvent etre modifier pendant l'execution du programme et sa taille peut changer pendant son execution
#car les elements y sont ajoutés ou retires

#Un tuple est un conteneur qui detient une serie des valeurs separees par virgule entre parentheses (x, y)
#ils snt comme des listes sauf qu'ils sont immutables donc vous ne pouvez pas changer son contenus une fois crees
#tout en contenant des types de donnees mixtes

valeur = input("Entrer certaines valeurs separer var des virgules : ")
list = valeur.split(",")
tuple = tuple(list)

print("List : ", list)
print("Tuple : ", tuple)