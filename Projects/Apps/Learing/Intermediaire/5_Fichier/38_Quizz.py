try:
    with open("fuck.txt") as f:
        print(f.read())
except:
    print("Erreur")
print()


f = open("fuck.txt", "r")
cont = f.read()
print(len(cont))
f.close()
print()

#la methode readlines return une list
#le mode utiliser qui permet d'ouvrir un fichier qui existe pour ajouter du contenus