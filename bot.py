import telebot
from flask import Flask, request

TOKEN = 8392489985:AAFzxKRngsUkbPHQWjHX8glygdjL8JYhtTg
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Я бот, развернутый на Render!")

if __name__ == "__main__":
    import os
    bot.remove_webhook()
    bot.set_webhook(url=f"https://olga-bot-2.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
