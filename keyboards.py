from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from config import config

class KeyCallback(CallbackData, prefix='button'):
    button: str
    loop: int

b = config.b

def keyboard_music() -> InlineKeyboardMarkup:

    builder = InlineKeyboardBuilder()
    for i in b:
        builder.add(InlineKeyboardButton(text=i, callback_data=KeyCallback(button=b[i][0], loop=b[i][1]).pack()))
        builder.adjust(5)

    return builder.as_markup()
