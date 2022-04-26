import logging
from telegram.ext import *
import responses

API_KEY = '5262961232:AAG7BFjvCXDk8gXr18cI8x9WGhMIJZOw-Yo'

# Configuration de l'enregistrement
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Salut a toi je suis IABot. Tu vas bien?')


def help_command(update, context):
    update.message.reply_text('Essaie d\'ecrire quelque chose et je ferais tout mon possible pour repondre')


def custom_command(update, context):
    update.message.reply_text('Ceci est une commande de customisation, vous pouvez ajouter n\'importe quels textes que vous voulez.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'Utilisateur ({update.message.chat.id}) a dit: {text}')

    # Reponse du Bot
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Enregistrement des erreurs
    logging.error(f'Update {update} caused error {context.error}')


# Exécution du programme
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commandes
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Enregistrer toutes les erreurs
    dp.add_error_handler(error)

    # Exécution le robot
    updater.start_polling(20.0)
    updater.idle()

main()