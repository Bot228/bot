import telebot
from command_handler import CommandHandler
from users_repository import UsersRepository
from states import State
from users_repository import UserInfo

from flask import Flask, request
import logging
import os

API_TOKEN = '411523498:AAGn-FBzFqXebb7IyJ-7KpkfHrJVVC0tJ6U'

bot = telebot.TeleBot(API_TOKEN)
users = UsersRepository("users")

handler = CommandHandler(bot, users)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    user_id = message.from_user.id
    if not users.exists(user_id):
        user_info = UserInfo(user_id, state=State.MAIN)
        users.save(user_info)
        handler.keyboard_in_tournaments(message)
    else:
        handler.keyboard_in_tournaments(message)


@bot.message_handler(commands=['call'])
def call(message):
    if ((str(message.from_user.id) == '442152076') or ((str(message.from_user.id) == '284137184'))):
        handler.make_advert(message)
    else:
        bot.send_message(message.chat.id, "У вас нет прав!")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

    if ((str(message.from_user.id) == '442152076') or ((str(message.from_user.id) == '284137184'))):
        if message.caption == '1':
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '1.jpg')
            os.remove(path)
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = '1.jpg'
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, "Фото добавлено")
            handler.kek1(src)
        elif message.caption == '2':
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '2.jpg')
            os.remove(path)
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = "2.jpg"
            with open("2.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, "Фото добавлено")
            handler.kek2(src)
        elif message.caption == '3':
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '3.jpg')
            os.remove(path)
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = "3.jpg"
            bot.reply_to(message, "Фото добавлено")
            with open("3.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            handler.kek3(src)
    else:
        bot.send_message(message.chat.id, 'У Вас нет прав!')

@bot.message_handler(content_types=['text'])
def sends(message):
    if (message.text == '📜 Расписание уроков'):
        handler.start1(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == '⏰ Расписание звонков'):
        handler.start2(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == '🍛 Меню в столовой'):
        handler.start3(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == '📝 График дежурств'):
        handler.start4(message)
        handler.keyboard_in_tournaments(message)

    if (message.text == '☎ Контакты'):
        bot.send_message(message.chat.id, 'Адрес:\n'
                                          'Город Павлодар, ул. Ленина д.12\n'
                                          'Телефон:\n'
                                          '53-47-14\n'
                                          'Email:\n'
                                          'lizey8@mail.ru\n')
        handler.keyboard_in_tournaments(message)

# Здесь пишем наши хэндлеры

# Проверим, есть ли переменная окружения Хероку (как ее добавить смотрите ниже)
if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook("https://botpls.herokuapp.com/" + API_TOKEN) # этот url нужно заменить на url вашего Хероку приложения
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)



