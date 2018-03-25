import command_parser as parser
from telebot import TeleBot, types
from telebot.types import Message
from users_repository import UsersRepository
import keyboard_helper

class CommandHandler:

    def __init__(self, bot: TeleBot, users: UsersRepository):
        self.bot = bot
        self.file_info1 = ''
        self.file_info2 = ''
        self.file_info3 = ''
        self.file_info4 = ''
        self.users = users


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

    def make_advert(self, message: Message):
        advert_text = parser.get_text_args(message.text)
        if not advert_text:
            self.bot.send_message(message.chat.id, 'Пустое сообщение')
        else:
            for info in self.users.read_all():
                try:
                    self.bot.send_message(info.user_id, advert_text)
                except:
                    print("Failed to send message to you")