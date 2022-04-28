#Ecrire un programme python pour accepeter un nom de fichier de l'utilisateur et imprime son extension

nom_fichier = input("Entrer le nom du fichier : ")
f_ext = nom_fichier.split(".")
print("L'extension du fichier est : " + repr(f_ext[-1]))