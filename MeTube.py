import os

import telebot

import request

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Mp3 or Mp4 File")

@bot.messsage_handler(commands=['Mp3'])
def send_message(message):
    bot.reply_to(message, "Provide me with link")

@bot.message_handler(commands=['Mp4'])
def send_message(message):
    bot.reply_to(message, "Provide me with link")

    
bot.infinity_polling()