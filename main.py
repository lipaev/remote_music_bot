import logging
import pyautogui
from random import choice

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, Message, BotCommand

from config import config
from filters import WritingOnFile, IsAdmin
from keyboards import keyboard_music, KeyCallback, keyboard_relingo

bot = Bot(config.tg_bot.token)
dp = Dispatcher()
admins_ids = config.tg_bot.admins_ids
buttons_names_b = list(map(lambda x: x[0], config.b.values()))
buttons_names_relingo = list(map(lambda x: x[0], config.relingo.values()))
handler = logging.FileHandler('logs.log', mode='w', encoding='utf-8')
handler.addFilter(WritingOnFile())
logging.basicConfig(level=logging.DEBUG,
                    format='{asctime}|{levelname:7}|{filename}:{lineno}|{name}|  {message}',
                    style='{',
                    handlers=[handler, logging.StreamHandler()])


async def message_music(message: Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.delete()
    await message.answer_sticker(choice(config.stickers), reply_markup=keyboard_music())

async def message_relingo(message: Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.delete()
    await message.answer_sticker(choice(config.stickers), reply_markup=keyboard_relingo())

async def callback_music(query: CallbackQuery, callback_data: KeyCallback):
    pyautogui.press(callback_data.button.split(';;;'), callback_data.loop)
    await query.answer()

async def set_main_menu(bot: Bot):

    main_menu_commands = [
        BotCommand(command='/music',
                   description='Musical buttons'),
        BotCommand(command='/relingo',
                   description='Relingo buttons')
    ]

    await bot.set_my_commands(main_menu_commands)

dp.callback_query.register(callback_music, KeyCallback.filter(F.button.in_([*buttons_names_b, *buttons_names_relingo])))
dp.message.register(message_music, Command(commands=["music", 'start']), IsAdmin())
dp.message.register(message_relingo, Command(commands=["relingo"]), IsAdmin())
dp.startup.register(set_main_menu)

if __name__ == "__main__":
    dp.run_polling(bot)