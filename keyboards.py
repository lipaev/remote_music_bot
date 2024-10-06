from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

def keyboard_music() -> InlineKeyboardMarkup:

    button_prev = InlineKeyboardButton(text='⏪', callback_data='prev')
    button_play = InlineKeyboardButton(text='⏯', callback_data='play')
    button_next = InlineKeyboardButton(text='⏩', callback_data='next')
    button_vup = InlineKeyboardButton(text='🔊 ⬆️', callback_data='vup')
    button_vdn = InlineKeyboardButton(text='🔉 ⬇️', callback_data='vdn')

    keyboard_music = InlineKeyboardMarkup(inline_keyboard=[
        [button_prev, button_play, button_next],
        [button_vdn, button_vup]
        ])

    return keyboard_music