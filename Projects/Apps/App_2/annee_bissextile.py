year = input("Annee que vous voulez essayer: ")
year_num = int(year)

if year_num % 4 == 0:
    print(year_num, "est une annee bissextile")
else:
    print(year_num, "n'est pas une annee bissextile")