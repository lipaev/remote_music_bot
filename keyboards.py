from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from config import config

class KeyCallback(CallbackData, prefix='button'):
    button: str
    loop: int

b = config.b
relingo = config.relingo

def keyboard_music() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(*[
        InlineKeyboardButton(text=i, callback_data=KeyCallback(button=b[i][0], loop=b[i][1]).pack())
        for i in list(b.keys())[:3]
    ])
    builder.row(*[
        InlineKeyboardButton(text=i, callback_data=KeyCallback(button=b[i][0], loop=b[i][1]).pack())
        for i in list(b.keys())[3:7]
    ])
    builder.row(*[
        InlineKeyboardButton(text=i, callback_data=KeyCallback(button=b[i][0], loop=b[i][1]).pack())
        for i in list(b.keys())[7:11]
    ])

    return builder.as_markup()

def keyboard_relingo() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        *[InlineKeyboardButton(text=i, callback_data=KeyCallback(button=relingo[i][0], loop=relingo[i][1]).pack())
        for i in list(relingo.keys())[:3]],
                width=1)

    builder.row(*[
        InlineKeyboardButton(text=i, callback_data=KeyCallback(button=relingo[i][0], loop=relingo[i][1]).pack())
        for i in list(relingo.keys())[3:6]
        ])

    return builder.as_markup()
