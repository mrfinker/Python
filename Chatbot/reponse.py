import random

R_EATING = "Je ne manges rien car je suis un robot !"
R_ADVICE = "si j'etais toi, j'irai sur internet et je taperai exactement ce que tu viens de me demander !"

def inconnu():
    reponse = ["pourriez-vous repeter s'il vous plait ? ",
                "...",
                "je n'ai rien compris.",
                "qu'est-ce que cela veut dire ?",
                "Oyo okomi kosala ngo na nko"][
        random.randrange(5)]
    return reponse