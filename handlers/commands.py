from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.exceptions import BotBlocked
from tools.logger import get_logger
from tools.database import db
from tools.bot import bot
from tools.messages import all_messages, all_keyboards, default
from keyboards.inline import Keyboard

kb = Keyboard()

async def start_menu(message: types.Message):
    logger.debug(f'user {message.from_user.id} pressed command /start.')
    uid = message.from_user.id
    uid_status = await db.get(table_name='users',
                              items=('status',),
                              condition={'tg_id': uid})
    match uid_status:
        # user is new
        case None:
            username = message.from_user.username
            language = default['language']
            await db.insert(table_name='users',
                            items={'tg_id': uid,
                                   'tg_name': message.from_user.first_name,
                                   'nickname': f'user-{uid}',
                                   'language': language,
                                   'flag': None,
                                   'status': None,
                                   'in_chat': None,
                                   'code': await db.get_unique_code(),
                                   'username': username})
            await bot.send_message(uid, all_messages['NICKNAME']['CREATE NICKNAME'][language])
            await db.update(table_name='users',
                            items={'status': 'without_nickname'},
                            condition={'tg_id': uid})
        # new user without nickname
        case 'without_nickname':
            language = await db.get(table_name='users',
                                    items=('language',),
                                    condition={'tg_id': uid})
            await bot.send_message(uid, all_messages['NICKNAME']['CREATE NICKNAME'][language])
        # user in menu
        case 'in_menu':
            language = await db.get(table_name='users',
                                    items=('language',),
                                    condition={'tg_id': uid})
            await bot.send_message(uid, all_messages['MENU'][language],
                                   reply_markup=kb.get('MENU KEYBOARD', language))
        # user in public chat
        case 'in_public_chat':
            chat_name = await db.get_chat_name(uid)
            chat_members_data = [i for i in await db.get_chat_members(uid, with_language=True)]
            await db.update_many(table_name='users',
                                 items={'status': 'in_menu', 'in_chat': None},
                                 condition={'tg_id': uid})
            if chat_members_data:
                nickname, flag = await db.get(table_name='users',
                                              items=('nickname', 'flag'),
                                              condition={'tg_id': uid})
                flag = '' if flag is None else f'[{flag}]'
                for member_data in chat_members_data:
                    member_uid, member_language = member_data
                    try:
                        await bot.send_message(chat_id=member_uid,
                                               parse_mode='html',
                                               text=all_messages['USER DISCONNECT'][member_language]\
                                                    .format(nickname, flag))
                    except BotBlocked as e:
                         logger.exception(e)
                         await db.update_many(table_name='users',
                                              items={'status': 'bot_blocked', 'in_chat': None},
                                              condition={'tg_id': member_uid})
            language = await db.get(table_name='users',
                                    items=('language',),
                                    condition={'tg_id': uid})
            await bot.send_message(chat_id=uid,
                                   parse_mode='html',
                                   text=all_messages['OFF PUBLIC'][language]\
                                        .format(all_keyboards['PUBLIC CHATS KEYBOARD']\
                                                             [f'{chat_name.upper()} BUTTON']\
                                                             ['NAME'][language].rstrip()))
            await bot.send_message(chat_id=uid,
                                   text=all_messages['MENU'][language],
                                   reply_markup=kb.get('MENU KEYBOARD', language))
        # user press command in other menus
        case _:
            language = await db.get(table_name='users',
                                    items=('language',),
                                    condition={'tg_id': uid})
            await bot.send_message(uid, all_messages['MENU'][language],
                                   reply_markup=kb.get('MENU KEYBOARD', language))
            await db.update(table_name='users',
                            items={'status': 'in_menu'},
                            condition={'tg_id': uid})


def commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start_menu, commands=['start', 'menu'])

logger = get_logger('main.handlers.commands.py')