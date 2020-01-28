from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import random

updater = Updater(token='1064584856:AAF9P6QEMj-F9o4585qeBR-7mY2-ciDCjLs', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TYPING_REPLY = range(3)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def roast(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Enihow is short")

def chiobu(update, context):
    file = "/Users/geraldine/Desktop/untitled folder"
    pic = random.choice(os.listdir(file))
    print(pic)
    pic = os.path.join(file, pic)
    print(pic)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(pic,'rb'))

def regular_choice(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Your {}? Yes, I would love to hear about that!'.format(text.lower()))

    return TYPING_REPLY


start_handler = CommandHandler('start', start)
roast_handler = CommandHandler('chiobu', chiobu)
regular_choice = CommandHandler('pick', regular_choice)
chiobu_handler = CommandHandler('roast', roast)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(roast_handler)
dispatcher.add_handler(chiobu_handler)
dispatcher.add_handler(regular_choice)
updater.start_polling()