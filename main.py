import logging
import pyautogui
from random import choice

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, Message

from config import config
from filters import WritingOnFile, IsAdmin
from keyboards import keyboard_music, KeyCallback


bot = Bot(config.tg_bot.token)
dp = Dispatcher()
admins_ids = config.tg_bot.admins_ids
handler = logging.FileHandler('logs.log', mode='w', encoding='utf-8')
handler.addFilter(WritingOnFile())
logging.basicConfig(level=logging.DEBUG,
                    format='{asctime}|{levelname:7}|{filename}:{lineno}|{name}|  {message}',
                    style='{',
                    handlers=[handler, logging.StreamHandler()])

backs = ['prevtrack', 'playpause', 'nexttrack', 'volumedown', 'volumeup', 'left', 'right']

async def message_music(message: Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer_sticker(choice(config.stickers), reply_markup=keyboard_music())

async def callback_music(query: CallbackQuery, callback_data: KeyCallback):
    await query.message.delete()
    for _ in range(int(callback_data.loop)):
        pyautogui.press(callback_data.button)
    await query.answer()
    await query.message.answer_sticker(choice(config.stickers), reply_markup=keyboard_music(), disable_notification=False)

dp.callback_query.register(callback_music, KeyCallback.filter(F.button.in_(backs)))
dp.message.register(message_music, Command(commands=["music", 'start']), IsAdmin())

if __name__ == "__main__":
    dp.run_polling(bot)