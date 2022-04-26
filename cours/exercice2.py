nom = input("Quel est votre nom : ")

while nom == "":
    nom = input("Quel est votre nom : ")

age = 0

while age == 0:
    age_str = input("Quel est votre age : ")
    try:
        age = int(age_str)
        age_next = age + 1
    except:
        print("ERREUR : Veuiller repeter s'il vous plait")
    
print("Votre nom est " + nom + ", vous avez " + str(age) + " ans " + "et l'an prochain vous aurez " + str(age_next) + " ans.")