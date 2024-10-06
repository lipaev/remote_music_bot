import logging
import pyautogui
from random import choice

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, Message

from config import config
from filters import WritingOnFile, IsAdmin
from keyboards import keyboard_music


bot = Bot(config.tg_bot.token)
dp = Dispatcher()
admins_ids = config.tg_bot.admins_ids
handler = logging.FileHandler('logs.log', mode='w', encoding='utf-8')
handler.addFilter(WritingOnFile())
logging.basicConfig(level=logging.DEBUG,
                    format='{asctime}|{levelname:7}|{filename}:{lineno}|{name}|  {message}',
                    style='{',
                    handlers=[handler, logging.StreamHandler()])


async def message_music(message: Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer_sticker(choice(config.stickers), reply_markup=keyboard_music())

async def callback_music(cal: CallbackQuery):
    if cal.data == 'prev':
        pyautogui.press('prevtrack')
        await cal.answer('Previous track')
    elif cal.data == 'play':
        pyautogui.press('playpause')
        await cal.answer('Play/Pause')
    elif cal.data == 'vup':
        for _ in range(4):
            pyautogui.press('volumeup')
        await cal.answer('Volume up')
    elif cal.data == 'vdn':
        for _ in range(4):
            pyautogui.press('volumedown')
        await cal.answer('Volume down')
    else:
        pyautogui.press('nexttrack')
        await cal.message.delete()
        await cal.message.answer_sticker(choice(config.stickers), reply_markup=keyboard_music(), disable_notification=False)

dp.callback_query.register(callback_music, F.data.in_(['prev', 'play', 'next', 'vdn', 'vup']))
dp.message.register(message_music, Command(commands=["music", 'start']), IsAdmin())

if __name__ == "__main__":
    dp.run_polling(bot)