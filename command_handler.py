
from telebot import TeleBot, types
from telebot.types import Message

import keyboard_helper


class CommandHandler:

    def __init__(self, bot: TeleBot):
        self.bot = bot
        self.file_info1 = ''
        self.file_info2 = ''
        self.file_info3 = ''
        self.file_info4 = ''

    def start1(self, message: Message):
        if self.file_info1 != '':
            self.bot.send_photo(message.chat.id, self.file_info1)

    def start2(self, message: Message):
        self.bot.send_photo(message.chat.id, 'https://content.foto.my.mail.ru/mail/faspo28/_myphoto/h-1.jpg')

    def start3(self, message: Message):
        if self.file_info2 != '':
            self.bot.send_photo(message.chat.id, self.file_info2)

    def start4(self, message: Message):
        if self.file_info3 != '':
            self.bot.send_photo(message.chat.id, self.file_info3)

    def kek1(self, message: Message):
        self.file_info1 = message

    def kek2(self, message: Message):
        self.file_info2 = message

    def kek3(self, message: Message):
        self.file_info3 = message

    def keyboard_in_tournaments(self, message: Message):
        keyboard = keyboard_helper.create_tournaments_keyboard()
        tournament_list = 'Список функций'
        self._send_keyboard(message.chat.id, tournament_list, keyboard)

    def _send_keyboard(self, chat_id: str, text:str, keyboard: types.ReplyKeyboardMarkup):
        self.bot.send_message(chat_id, text, reply_markup=keyboard, parse_mode="Markdown")