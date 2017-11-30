#Citation_Bot cites a French quote by command or every three hours.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
updater = Updater(token='407075567:AAH5LJy0RY5ap7ldRKSChO2EM9CeckS9YG8')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Bienvenue !")


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Je suis desolé, je ne comprends pas !")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
