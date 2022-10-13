from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher import Dispatcher
from aiogram import types
from tools.logger import get_logger
from tools.database import db

async def bot_blocked(update: types.Update, exception: BotBlocked, uid=None):
    logger.debug(f'Exception {exception}: {update}')
    if update.message:
        uid = update.message.from_user.id
    if update.callback_query:
        uid = update.callback_query.message.from_user.id
    print(uid)
    try:
        await db.update_many(table_name='users',
                            items={'status': 'bot_blocked', 'in_chat': None},
                            condition={'tg_id': uid})
    except Exception as e:
        logger.exception(e)
    return True

def error_handlers(dp: Dispatcher):
    dp.register_errors_handler(bot_blocked, exception=BotBlocked)

logger = get_logger('main.handlers.errors.py')
