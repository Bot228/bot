import telebot
from command_handler import CommandHandler
from persistent_storage1.users_repository import UsersRepository
from states import State

API_TOKEN = '480759169:AAFbS77iCMmIeR87O0i9DH0QxVwZ5WqTFDs'

bot = telebot.TeleBot(API_TOKEN)

handler = CommandHandler(bot)
users = UsersRepository("persistent_storage1\\storage\\users")


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    user_id = message.from_user.id
    if not users.exists(user_id):
        users.save(user_id, state=State.MAIN)
        #file = open(str(user_id) + '.txt', "w")
        #file.write("Корзина:\n")
        #file.close()
        handler.keyboard_in_tournaments(message)
    else:
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
