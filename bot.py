import telebot
from flask import Flask, request

TOKEN = "сюда вставь свой токен от BotFather"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def hello():
    return "Бот работает!"

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Я твой бот 🤖")

if __name__ == "__main__":
    bot.polling()
