from aiogram import types
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher import Dispatcher
from tools.logger import get_logger
from tools.database import db
from tools.bot import bot
from tools.messages import all_messages


async def message(message: types.Message):
    await bot.send_message(message.from_user.id, message.message_id)
    await bot.delete_message(message.from_user.id, message.message_id)

def message_handlers(dp: Dispatcher):
    dp.register_message_handler(message, content_types=['text', 'document', 'audio', 'photo', 'sticker', 'video',
                                                        'voice', 'location', 'contact', 'video_note', 'animation'])

logger = get_logger('main.handlers.messages.py')