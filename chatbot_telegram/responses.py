import re
import random
import liens

lien_A = liens.A

def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        process_message(message, ['bonjour', 'salut'], 'Bonjour!'),
        process_message(message, ['bye', 'aurevoir', 'plus', 'tard'], 'Aurevoir!'),
        process_message(message, ['comment', 'vas'], 'Je vais tres bien!'),
        process_message(message, ["t'", "appelle"], 'Mon nom est IABot, heureux de faire votre connaissance!'),
        process_message(message, ['besoin', 'aide'], 'je ferais de mon mieux pour vous aidez!'),
        process_message(message, ['cree', 'qui'], 'J\'etais cree par Caleb Kiangebeni, Mutshipay felix et Ngoy Selemani!'),
        process_message(message, ['cree', 'quand'], 'J\'etais cree Vendredi le 11 fevrier 2022 à l\'Université de Kinshasa'),
        process_message(message, ['merci'], 'Merci pareillement'),
        process_message(message, ['fais', 'quoi'], 'je ne fais rien et toi ?'),
        process_message(message, ['je', 'vais', 'bien'], 'Super cool, comment se passe la journee?'),
        process_message(message, ['je', 'vais', 'super', 'bien'], 'Heureux de l\'entendre'),
        process_message(message, ['je', 'vais', 'tres', 'mal'], 'Desolé pour toi, mais j\'espere que tout ira bien ... mais si tu veux tu peux acheter ça ---> '+''+lien_A),
        process_message(message, ['je', 'vais', 'mal'], 'Desolé pour toi, j\'espere que tout ira bien et tu fera l\'effort d\'aller mieux')
        # Add more responses here
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = ["pourriez-vous repeter s'il vous plait ? ",
                "...",
                "je n'ai rien compris.",
                "qu'est-ce que cela veut dire ?",
                "Oyo okomi kosala ngo na nko",
                "Je n'ai pas compris ce que vous venez d'écrire."][
        random.randrange(5)]
    
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response

# Test your system
# get_response('What is your name bruv?')
# get_response('Can you help me with something please?')
