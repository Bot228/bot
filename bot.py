import telebot
import logging
from command_handler import CommandHandler

from telebot import TeleBot, types

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

handler = CommandHandler(bot)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    '''bot.reply_to(message, """\
Привет! 
Я тестовый бот, и умею я пока немного. Напиши мне и я отвечу!\
""")'''
    handler.keyboard_in_tournaments(message)

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
        if ((str(message.from_user.id) == '442152076') or ((str(message.from_user.id) == '284137184'))):
            file_info = message.photo[len(message.photo) - 1].file_id
            if message.caption == '1':
                handler.kek1(file_info)
            elif message.caption == '2':
                    handler.kek2(file_info)
            elif message.caption == '3':
                    handler.kek3(file_info)
        else:
            bot.send_message(message.chat.id, 'У Вас нет прав')

@bot.message_handler(content_types=['text'])
def sends(message):
    if (message.text == '📜 Расписание уроков'):
        handler.start1(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == u'\U0001F374 Расписание звонков'):
        handler.start2(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == u'\U0001F0CF Меню в столовой'):
        handler.start3(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == u'\U0001F697 График дежурств'):
        handler.start4(message)
        handler.keyboard_in_tournaments(message)

bot.polling(none_stop=True)