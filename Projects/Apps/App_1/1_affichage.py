# écrire un programme Python pour imprimer la chaîne suivante dans un format spécifique
import sys
a = 5
b =10

print("La reponse est ", 3 * 23)
print(a, end=" ") #ajoute un espace au lieu d'une nouvelle ligne
print #affiche une nouvelle ligne
print() #vous devez appeler la fonction
print()
print("fatal error", file=sys.stderr)
print(a, b) #imprime repr((a, b))
print((a, b)) #ne pas le meme affichage que print(a, b)
print("Twinkle, twinkle, little star,\n\tHow i wonder what you are!\n\t\tU above the world s high,\n\tLike a diamond in the sky,\nTwinkle, twinkle, little star,\n\tHow  wonder what you are!")