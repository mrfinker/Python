#czeci est pour ecrire dans un fichier, si il n'existe pas il le cree, si il existe deja il le remplace par le meme nom avec les nouveaux contenus
file = open("nouvelle_fichier_test.txt", "w")
file.write("Ceci est pour ecrire dans le fichier")
file.close
print()


#ceci pour ajouter du contenu(une ligne) dans un fichier qui existe
file = open("nouvelle_fichier_test.txt", "a")
file.write("\nvini vidi vici")
file.close()
print()


message = "Bonjour a tout le monde"
file = open("fuck.txt", "w")
nbr_ecrit = file.write(message)
print(nbr_ecrit)
file.close()
print()