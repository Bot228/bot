from typing import List

from telebot import types

from tournaments import ButtonType


def create_keyboard(row_width: int, buttons: List[ButtonType]) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*[types.KeyboardButton(str(button)) for button in buttons])
    return keyboard

def create_tournaments_keyboard() -> types.ReplyKeyboardMarkup:
    buttons = [ButtonType.Soccer, ButtonType.Salad, ButtonType.Poker,ButtonType.Bag, ButtonType.Pizza]
    return create_keyboard(row_width=2, buttons=buttons)