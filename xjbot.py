import os
import telebot
from time import sleep

# Use environment variable for bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! XJbot is now running on Render!")

# Keep the bot running
print("Bot is polling...")
bot.polling(none_stop=True)