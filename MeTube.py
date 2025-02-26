import os

import telebot

import yt_dlp

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Send /mp3 or /mp4 followed by the YouTube link.")

@bot.message_handler(commands=['mp3'])
def download_mp3(message):
    url = message.text.split(" ", 1)[-1]
    if not url.startswith("http"):
        bot.reply_to(message, "Please provide a valid YouTube link.")
        return

    try:
        output_file = "downloaded_audio.mp3"
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_file,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'cookies': 'cookies.txt'  # Use exported cookies
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        with open(output_file, "rb") as audio_file:
            bot.send_audio(message.chat.id, audio_file)

        os.remove(output_file)  # Cleanup

    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


@bot.message_handler(commands=['Mp4'])
def send_message(message):
    bot.reply_to(message, "Provide me with link")



    



    
bot.infinity_polling()