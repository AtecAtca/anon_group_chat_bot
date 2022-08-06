from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.exceptions import BotBlocked
from tools.logger import get_logger
from tools.database import db
from tools.bot import bot
from tools.messages import all_messages
from keyboards.inline import get_menu_keyboard

async def start(message: types.Message):
    logger.debug(f'user {message.from_user.id} pressed command /start.')
    uid = message.from_user.id
    uid_status = await db.get_status(uid)
    language = await db.get_language(uid)

    match uid_status:
        # user is new
        case None:
            text = all_messages['NICKNAME']['CREATE NICKNAME'][language]
            await db.register_new_user(uid, message, language)
            await bot.send_message(uid, text)
            await db.update_status(uid, 'without_nickname')
        # new user without nickname
        case 'without_nickname':
            text = all_messages['NICKNAME']['CREATE NICKNAME'][language]
            await bot.send_message(uid, text)

        case 'in_menu':
            text = all_messages['MENU'][language]
            keyboard = get_menu_keyboard(language)
            await bot.send_message(uid, text, reply_markup=keyboard)


def commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])

logger = get_logger('main.handlers.commands.py')