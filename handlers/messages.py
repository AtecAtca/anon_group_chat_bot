from aiogram import types
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher import Dispatcher
from tools.logger import get_logger
from tools.database import db
from tools.bot import bot
from tools.messages import all_messages, all_flags, default
from keyboards.inline import Keyboard

kb = Keyboard()

async def message(message: types.Message):
    logger.debug(f'user {message.from_user.id} write message {message.text}')
    uid = message.from_user.id
    uid_status, language = await db.get(table_name='users',
                                        items=('status', 'language'),
                                        condition={'tg_id': uid})
    language = default['language'] if language is None else language
    match uid_status:
        # new user without nickname or user edit nickname
        case 'without_nickname' | 'in_set_nickname':
            nickname = message.text
            if nickname is None:
                await bot.delete_message(uid, message.message_id)
                logger.debug(f'delete message-{message.message_id}')
            else:
                # if nickname is too long
                if len(nickname) > 16:
                    await bot.send_message(uid, all_messages['NICKNAME']['TOO LONG NICKNAME'][language])
                # if nickname have wrong symbols
                elif not db.is_nickname_in_all_symbols(nickname):
                    await bot.send_message(uid, all_messages['NICKNAME']['WRONG SYMBOLS IN NICKNAME'][language])
                # if nickname is unique -> get status 'in_menu'
                elif await db.get(table_name='users',
                                  items=('nickname',),
                                  condition={'nickname': nickname}) is None:
                    await db.update(table_name='users',
                                    items={'nickname': nickname},
                                    condition={'tg_id': uid})
                    await bot.send_message(uid, all_messages['NICKNAME']['NICKNAME SAVED'][language].format(nickname),
                                           parse_mode='html')
                    await bot.send_message(uid, all_messages['MENU'][language],
                                           reply_markup=kb.get('MENU KEYBOARD',language))
                    await db.update(table_name='users',
                                    items={'status': 'in_menu'},
                                    condition={'tg_id': uid})
                # if nickname not unique
                else:
                    await bot.send_message(uid, all_messages['NICKNAME']['NOT UNIQUE NICKNAME'][language])

        # user edit flag
        case 'in_set_flag':
            flag = message.text
            if flag in all_flags:
                nickname = await db.get(table_name='users',
                                        items=('nickname',),
                                        condition={'tg_id': uid})
                await db.update(table_name='users',
                                items={'flag': flag},
                                condition={'tg_id': uid})
                await bot.send_message(uid, all_messages['FLAG SAVED'][language].format(flag), parse_mode='html')

                await bot.send_message(chat_id=uid,
                                       text=all_messages['SETTINGS'][language].format(nickname, language, flag),
                                       parse_mode='html',
                                       reply_markup=kb.get('SETTINGS KEYBOARD', language))
                await db.update(table_name='users',
                                items={'status': 'in_settings'},
                                condition={'tg_id': uid})
            else:
                await bot.send_message(uid, all_messages['WRONG FLAG'][language])

        # user in public chat
        case 'in_public_chat':
            chat_members = [i[0] for i in await db.get_chat_members(uid)]
            if chat_members:
                nickname, flag = await db.get(table_name='users',
                                              items=('nickname', 'flag'),
                                              condition={'tg_id': uid})
                flag = '' if flag is None else f'[{flag}]'
                signature = f'{nickname}{flag}'
                for member in chat_members:
                    try:
                        await send_message(message, member, signature=signature)
                    except BotBlocked as e:
                        logger.exception(e)
                        await db.update_many(table_name='users',
                                             items={'status': 'bot_blocked', 'in_chat': None},
                                             condition={'tg_id': member})
        case 'bot_blocked':
            language = await db.get(table_name='users',
                                    items=('language',),
                                    condition={'tg_id': uid})
            await bot.send_message(uid, all_messages['MENU'][language],
                                   reply_markup=kb.get('MENU KEYBOARD', language))
            await db.update(table_name='users',
                            items={'status': 'in_menu'},
                            condition={'tg_id': uid})
        # user write message in other menus
        case _:
            await bot.delete_message(uid, message.message_id)
            logger.debug(f'delete message-{message.message_id}')





async def send_message(message: types.Message, member, signature):
    if message.text is None:
        text = f'<code>{signature}</code>'
    else:
        text = f'<code>{signature}:</code>\n{message.text}'
    try:
        if message.sticker:
            await bot.send_sticker(member, sticker=message.sticker.file_id)
        elif message.photo:
            await bot.send_photo(member, photo=message.photo[0].file_id, parse_mode='html', caption=text)
        elif message.animation:
            await bot.send_animation(member, animation=message.animation.file_id, parse_mode='html', caption=signature)
        elif message.video:
            await bot.send_video(member, video=message.video.file_id, parse_mode='html', caption=text)
        elif message.audio:
            await bot.send_audio(member, audio=message.audio.file_id, parse_mode='html', caption=text)
        elif message.document:
            await bot.send_document(member, document=message.document.file_id, parse_mode='html', caption=text)
        elif message.voice:
            await bot.send_voice(member, voice=message.voice.file_id, parse_mode='html', caption=text)
        else:
            await bot.send_message(member, text=text, parse_mode='html')
    except BotBlocked as e:
        pass

def message_handlers(dp: Dispatcher):
    dp.register_message_handler(message, content_types=['text', 'document', 'audio', 'photo', 'sticker', 'video',
                                                        'voice', 'location', 'contact', 'video_note', 'animation'])

logger = get_logger('main.handlers.messages.py')