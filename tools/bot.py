from aiogram.dispatcher import Dispatcher
from aiogram import Bot
import os
from tools.logger import get_logger

#TOKEN = os.environ.get('TOKEN') # web
TOKEN = os.getenv('TOKEN')
logger = get_logger('main.tools.bot.py')

try:
    bot = Bot(TOKEN)
except Exception as e:
    logger.exception(e)
else:
    logger.info('Telegram bot connected successfully.')
    dp = Dispatcher(bot)



