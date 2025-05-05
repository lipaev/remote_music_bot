from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from config import config

class KeyCallback(CallbackData, prefix='button'):
    button: str
    loop: int

b = config.b
relingo = config.relingo
mov = config.movies

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

    builder.row(*[
        InlineKeyboardButton(text=i, callback_data=KeyCallback(button=relingo[i][0], loop=relingo[i][1]).pack())
        for i in list(relingo.keys())[:3]],
                width=1)

    builder.row(*[
        InlineKeyboardButton(text=i, callback_data=KeyCallback(button=relingo[i][0], loop=relingo[i][1]).pack())
        for i in list(relingo.keys())[3:7]
        ])

    builder.row(*[
        InlineKeyboardButton(text=i, callback_data=KeyCallback(button=relingo[i][0], loop=relingo[i][1]).pack())
        for i in list(relingo.keys())[7:]],
                width=1)

    return builder.as_markup()

def keyboard_relingo_reply() -> ReplyKeyboardMarkup:
    keys = list(relingo.keys())[3:]  # без первых трёх
    rows = []
    # Первые два ряда по 2 кнопки, затем по одной в каждом ряду
    for i in range(0, min(4, len(keys)), 2):
        rows.append([KeyboardButton(text=keys[i]), KeyboardButton(text=keys[i+1])])
    for i in range(4, len(keys)):
        rows.append([KeyboardButton(text=keys[i])])
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=False)

def keyboard_movies_reply() -> ReplyKeyboardMarkup:
    keys = list(mov.keys())
    rows = []
    rows.append([KeyboardButton(text=keys[0]), KeyboardButton(text=keys[1])])
    rows.append([KeyboardButton(text=keys[2]), KeyboardButton(text=keys[3])])
    rows.append([KeyboardButton(text=keys[4])])
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=False)