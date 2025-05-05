import logging
import pyautogui
from random import choice

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, Message, BotCommand

from config import config
from filters import WritingOnFile, IsAdmin
from keyboards import keyboard_music, KeyCallback, keyboard_relingo, keyboard_relingo_reply, keyboard_movies_reply

bot = Bot(config.tg_bot.token)
dp = Dispatcher()
admins_ids = config.tg_bot.admins_ids
buttons_names_b = list(map(lambda x: x[0], config.b.values()))
buttons_names_relingo = list(map(lambda x: x[0], config.relingo.values()))
buttons_names_movies = list(map(lambda x: x[0], config.movies.values()))
handler = logging.FileHandler('logs.log', mode='w', encoding='utf-8')
handler.addFilter(WritingOnFile())
logging.basicConfig(level=logging.DEBUG,
                    format='{asctime}|{levelname:7}|{filename}:{lineno}|{name}|  {message}',
                    style='{',
                    handlers=[handler, logging.StreamHandler()])


async def message_music(message: Message):
    await message.delete()
    await message.answer_sticker(choice(config.stickers), reply_markup=keyboard_music())

async def message_relingo(message: Message):
    await message.delete()
    await message.answer_sticker(choice(config.stickers), reply_markup=keyboard_relingo())

async def message_relingo_reply(message: Message):
    await message.delete()
    await message.answer_sticker(choice(config.stickers), reply_markup=keyboard_relingo_reply())

async def message_movies_reply(message: Message):
    await message.delete()
    await message.answer_sticker(choice(config.stickers), reply_markup=keyboard_movies_reply())

async def handle_relingo_reply_button(message: Message):
    await message.delete()
    text = message.text
    # Проверяем, что текст — одна из кнопок relingo (без первых трёх)
    keys = list(config.relingo.keys())[3:]
    if text in keys:
        button, loop = config.relingo[text]
        pyautogui.press(button.split(';;;'), loop)
    else:
        await message.answer("Неизвестная команда.")

async def handle_movies_reply_button(message: Message):
    await message.delete()
    text = message.text
    # Проверяем, что текст — одна из кнопок relingo (без первых трёх)
    keys = list(config.movies.keys())
    if text in keys:
        button, loop = config.movies[text]
        pyautogui.press(button.split(';;;'), loop)
    else:
        await message.answer("Неизвестная команда.")

async def callback_music(query: CallbackQuery, callback_data: KeyCallback):
    pyautogui.press(callback_data.button.split(';;;'), callback_data.loop)
    await query.answer()

async def set_main_menu(bot: Bot):

    main_menu_commands = [
        BotCommand(command='/music',
                   description='Musical buttons'),
        BotCommand(command='/relingo',
                   description='Relingo buttons'),
        BotCommand(command='/reply',
                   description='Keyboard buttons'),
        BotCommand(command='/movies',
                   description='Keyboard movies buttons')
    ]

    await bot.set_my_commands(main_menu_commands)

dp.callback_query.register(
    callback_music,
    KeyCallback.filter(F.button.in_([*buttons_names_b, *buttons_names_relingo]))
    )
dp.message.register(handle_relingo_reply_button, F.text.in_(list(config.relingo.keys())[3:]), IsAdmin())
dp.message.register(handle_movies_reply_button, F.text.in_(list(config.movies.keys())), IsAdmin())
dp.message.register(message_music, Command(commands=["music", 'start']), IsAdmin())
dp.message.register(message_relingo, Command(commands=["relingo"]), IsAdmin())
dp.message.register(message_relingo_reply, Command(commands=["reply"]), IsAdmin())
dp.message.register(message_movies_reply, Command(commands=["movies"]), IsAdmin())
dp.startup.register(set_main_menu)

if __name__ == "__main__":
    dp.run_polling(bot)