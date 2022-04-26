import re
import reponse as long

def message_proba(message_utilisateur, mots_reconnu, reponse_unique=False, mots_requis=[]):
    message_certain = 0
    has_mots_requis = True

    # compte combien des mots sont presents dans le meme message predefinis
    for mot in message_utilisateur:
        if mot in mots_reconnu:
            message_certain += 1

    # Calculate des mots reconnus entrer par l'utilisateur
    pourcentage = float(message_certain) / float(len(mots_reconnu))

    # verifie si les mots reconnus sont en type String
    for mot in mots_requis:
        if mot not in message_utilisateur:
            has_mots_requis = False
            break

    # Must either have the required words, or be a single response
    if has_mots_requis or reponse_unique:
        return int(pourcentage * 100)
    else:
        return 0

def verification_tout_messages(message):
    grande_prob_liste = {}

    # Simplification des reponses crée et ajout
    def reponse(bot_reponse, liste_de_mots, reponse_unique=False, mots_requis=[]):
        nonlocal grande_prob_liste
        grande_prob_liste[bot_reponse] = message_proba(message, liste_de_mots, reponse_unique, mots_requis)

    # Reponses -------------------------------------------------------------------------------------------------------
    reponse('Bonjour et bienvenue je m\'appelle finkerbot, comment vas-tu ?', ['bonjour', 'Salut'], reponse_unique=True)
    reponse('Alors je ne vous sers à rien, poser une autre question ou je vous serez utile', ['ne', 'sais', 'pas'], reponse_unique=True)
    reponse('A plus tard', ['bye', 'aurevoir'], reponse_unique=True)
    reponse('Je vais bien et toi ?', ['comment', 'vas', 'tu'], mots_requis=['comment', 'tu', 'vas'])
    reponse('Tship', ['comment', 'vas', 'tu'], mots_requis=['comment'])
    reponse('Desolé pour toi, je ne saurais te consoler mais j\'espere que tout ira bien, bref à part ça ?', ['je', 'vais', 'mal'], mots_requis=['vais', 'mal'])
    reponse('Desolé pour toi, j\'espere que tout ira bien et tu fera l\'effort d\'aller mieux, bref à part ça ?', ['je', 'vais', 'mal'], mots_requis=['mal'])
    reponse('Heureux de l\'entendre', ['je', 'vais', 'bien'], mots_requis=['bien'])
    reponse('Super cool', ['je', 'vais', 'bien'], mots_requis=['bien', 'vais'])
    reponse('Merci pareillement', ['merci'], reponse_unique=True)
    reponse('Merci, je t\'aime aussi', ['j\'aime', 'finkerbot'], mots_requis=['j\'aime', 'finkerbot'])
    reponse('J\'etais cree par Caleb Kiangebeni, Mutshipay felix et Ngoy Selemani', ['qui', 'cree'], mots_requis=['qui', 'cree'])
    reponse('J\'etais cree Vendredi le 11 fevrier 2022 à l\'Université de Kinshasa', ['quand', 'cree'], mots_requis=['quand', 'cree'])

    # Longueur des reponses
    reponse(long.R_ADVICE, ['give', 'advice'], mots_requis=['advice'])
    reponse(long.R_EATING, ['que', 'tu', 'manges'], mots_requis=['tu', 'manges'])
    reponse(long.R_EATING, ['que', 'tu', 'mange'], mots_requis=['tu', 'mange'])

    meilleur_correspondance = max(grande_prob_liste, key=grande_prob_liste.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.inconnu() if grande_prob_liste[meilleur_correspondance] < 1 else meilleur_correspondance

# Utiliser pour recevoir les reponses
def recevoir_reponse(entrer_utilisateur):
    decouper_message = re.split(r'\s+|[,;?!.-]\s*', entrer_utilisateur.lower())
    reponse = verification_tout_messages(decouper_message)
    return reponse

# Teste reponse du systeme
while True:
    print('finkerBot: ' + recevoir_reponse(input('Vous: ')))