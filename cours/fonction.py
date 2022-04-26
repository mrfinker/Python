def demander_age():
    age_d = 0
    while age_d == 0:
        age_str = input("Quel est votre age : ")
        try:
            age_d = int(age_str)
            # age_next_d = age_d + 1
        except:
            print("ERREUR : Veuiller repeter s'il vous plait")
    return age_d

def demander_nom():
    nom_d = input("Quel est votre nom : ")
    while nom_d == "":
            nom_d = input("Quel est votre nom : ")
    return nom_d

nom = demander_nom()
age = demander_age()
age_next_d = demander_age()

print("Votre nom est " + nom + ", vous avez " + str(age) + " ans ")
# print("et l'an prochain vous aurez " + str(age_next) + " ans.")