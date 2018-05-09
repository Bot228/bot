from flask import Flask, request
import telebot
import os

server = Flask(__name__)
TOKEN  = '411523498:AAGn-FBzFqXebb7IyJ-7KpkfHrJVVC0tJ6U'
bot = telebot.TeleBot(TOKEN) 
port = int(os.environ.get("PORT", 5000))

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://botpls.herokuapp.com") 
    return "!", 200

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_messages(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message])
    return "!", 200

@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, 'Hi')

server.run(host='0.0.0.0', port=port)