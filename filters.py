from aiogram.filters import BaseFilter
from aiogram.types import Message
from logging import Filter, LogRecord
from config import config

class IsAdmin(BaseFilter):
    """
    Filter for admins
    """
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in config.tg_bot.admins_ids

class WritingOnFile(Filter):
    """Filter for writing on file"""
    # Переменная рекорд ссылается на объект класса LogRecord
    def filter(self, record: LogRecord) -> bool:
        return record.levelname in ['WARNING', 'ERROR', 'CRITICAL']
