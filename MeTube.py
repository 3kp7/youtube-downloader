import os

import telebot

from pytube import Youtube

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Mp3 or Mp4 File")

@bot.message_handler(commands=['Mp3'])
def send_message(message):
    bot.reply_to(message, "Provide me with link")

@bot.message_handler(commands=['Mp4'])
def send_message(message):
    bot.reply_to(message, "Provide me with link")

def mp3_video(url):
    video_caller = Youtube(url)
    print(video_caller.title)
    video_caller.stream.filter(progressive=True,extention="mp3".order_by(
            'resolution').desc().first().download())
            print("done")

    
bot.infinity_polling()