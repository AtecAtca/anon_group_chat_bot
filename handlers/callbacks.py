from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.exceptions import BotBlocked
from tools.messages import all_messages
from tools.logger import get_logger
from tools.database import db
from tools.bot import bot


def callback_handlers(dp: Dispatcher):
    pass

logger = get_logger('main.handlers.callbacks.py')