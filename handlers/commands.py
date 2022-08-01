from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.exceptions import BotBlocked
from tools.logger import get_logger
from tools.database import db
from tools.bot import bot
from tools.messages import all_messages


async def start(message: types.Message):
    pass


def commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])

logger = get_logger('main.handlers.commands.py')