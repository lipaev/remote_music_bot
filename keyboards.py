from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class KeyCallback(CallbackData, prefix='button'):
    button: str
    loop: int

b = {'⏪': ('prevtrack', 1),
         '⏯': ('playpause', 1),
         '⏩': ('nexttrack', 1),
         '🔊 ⬆️': ('volumedown', 4),
         '🔉 ⬇️': ('volumeup', 4),
         '⬅️': ('left', 1),
         '➡️': ('right', 1),
         'J': ('j', 1),
         'L': ('l', 1),
         'K': ('k', 1)}

def keyboard_music() -> InlineKeyboardMarkup:

    builder = InlineKeyboardBuilder()
    for i in b:
        builder.add(InlineKeyboardButton(text=i, callback_data=KeyCallback(button=b[i][0], loop=b[i][1]).pack()))
        builder.adjust(5)

    return builder.as_markup()
