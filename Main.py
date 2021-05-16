#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

import logging, os, json, random
from modules import ControllerTasks
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)
token = os.environ["TOKEN_OMD_BOT"]

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    pass
    # first_name = update_object.get("message").get("chat").get("first_name")
    # print(first_name)
#    greeting_message = read_greetings()
 #   update.message.reply_text(greeting_message.format(update.message.chat.first_name))

def help_command(update, context):
    update.message.reply_text(get_help_message())

# my functions...
def fun(update, context):
    return None

def echo(update, context):
    # Echo the user message.
    update.message.reply_text(update.message.text)

def get_help_message():
    route = ""
    # return open(os.environ["PP_ROUTE"] + route).read()
    return "Hola"

def get_all_tasks_for_today(update, context):
    text = update.message.text     # text from the user from telegram
    username = text[5:len(text)]
    message = ControllerTasks.get_all_tasks_for_today(username)
    update.message.reply_text(message)   # text to resp

def reply_message(update, context):
    if (update.message.text.lower().find("hol") >= 0):
        update.message.reply_text("Hola we")
    #elif (update.message.text != "help" and update.message.text != "start"):
    else:
        random_answers = ["me invocaste wey", "no toy", "ke", "zzzz", ":v", ":)", "¿ke kieres ahora?", "me juí"]
        index = random.randint(0, len(random_answers) - 1)
        update.message.reply_text(random_answers[index])

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    # dp.add_handler(CommandHandler("clima", answer_weather))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ayuda", help_command))
    dp.add_handler(CommandHandler("hoy", get_all_tasks_for_today))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__': main()
