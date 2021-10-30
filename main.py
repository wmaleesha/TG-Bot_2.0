import os
import telebot


bot = telebot.TeleBot("2076975842:AAFPwYImUZh4o5NdUG2W9-7OL9XqSdsVLQk")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Uvindu Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://youtube.com/c/Uvindubro")



bot.polling()
