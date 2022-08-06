from aiogram import types
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher import Dispatcher
from tools.logger import get_logger
from tools.database import db
from tools.bot import bot
from tools.messages import all_messages
from keyboards.inline import get_menu_keyboard




async def message(message: types.Message):
    logger.debug(f'user {message.from_user.id} write message {message.text}')
    uid = message.from_user.id
    uid_status = await db.get_status(uid)
    language = await db.get_language(uid)

    match uid_status:
        # user is new
        case None:
            await bot.delete_message(uid, message.message_id)
            logger.debug(f'delete message-{message.message_id}')

        # new user without nickname
        case 'without_nickname':
            nickname = message.text
            if nickname is None:
                await bot.delete_message(uid, message.message_id)
                logger.debug(f'delete message-{message.message_id}')
            else:
                # if nickname is too long
                if len(nickname) > 16:
                    text = all_messages['NICKNAME']['TOO LONG NICKNAME'][language]
                    await bot.send_message(uid, text)
                # if nickname have wrong symbols
                elif not db.is_nickname_in_all_symbols(nickname):
                    text = all_messages['NICKNAME']['WRONG SYMBOLS IN NICKNAME'][language]
                    await bot.send_message(uid, text)
                # if nickname is unique -> get status 'in_menu'
                elif await db.is_nickname_unique(nickname):
                    text = all_messages['NICKNAME']['NICKNAME SAVED'][language].format(nickname)
                    await db.update_nickname(uid, nickname)
                    await db.update_status(uid, 'in_menu')
                    await bot.send_message(uid, text)
                    text = all_messages['MENU'][language]
                    keyboard = get_menu_keyboard(language)
                    await bot.send_message(uid, text, reply_markup=keyboard)
                # if nickname not unique
                else:
                    text = all_messages['NICKNAME']['NOT UNIQUE NICKNAME'][language]
                    await bot.send_message(uid, text)

        case 'in_menu':
            await bot.delete_message(uid, message.message_id)
            logger.debug(f'delete message-{message.message_id}')






def message_handlers(dp: Dispatcher):
    dp.register_message_handler(message, content_types=['text', 'document', 'audio', 'photo', 'sticker', 'video',
                                                        'voice', 'location', 'contact', 'video_note', 'animation'])

logger = get_logger('main.handlers.messages.py')