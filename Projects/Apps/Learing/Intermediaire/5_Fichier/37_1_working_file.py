try:
    f = open("fuck.txt")
    cont = f.read()
    print(cont)
finally:
    f.close()
print()


try:
    f = open("fuck.txt")
    print(f.read())
    print(1/0)
finally:
    f.close()
print()


#une autre maniere de le faire, en creant une variable temporaire appeler 'f'
#le fichier est automatiquement fermer a la fin "with"
with open("fuck.txt") as f:
    print(f.read())