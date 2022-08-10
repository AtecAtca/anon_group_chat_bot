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
                            items={
                                'tg_id': uid,
                                'tg_name': message.from_user.first_name,
                                'nickname': f'user-{uid}',
                                'language': language,
                                'flag': None,
                                'status': None,
                                'in_chat': None,
                                'code': await db.get_unique_code(),
                                'username': username})
            #await db.register_new_user(uid, message, language)
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
            in_chat, language, nickname, flag = await db.get(table_name='users',
                                                             items=('in_chat', 'language', 'nickname', 'flag'),
                                                             condition={'tg_id': uid})
            chat_name, chat_members = await db.get(table_name='chats',
                                                   items=('chat_name', 'chat_members'),
                                                   condition={'chat_code': in_chat})
            await db.update(table_name='chats',
                            items={'chat_members': uid},
                            array_func='array_remove',
                            condition={'chat_code': in_chat})

            if len(chat_members) > 1:
                if flag is None:
                    flag = ''
                else:
                    flag = f'[{flag}]'

                for member in chat_members:
                    if member != uid:
                        member_language = await db.get(table_name='users',
                                                items=('language',),
                                                condition={'tg_id': member})
                        try:
                            await bot.send_message(chat_id=member,
                                                   parse_mode='html',
                                                   text=all_messages['USER DISCONNECT'][member_language]\
                                                        .format(nickname, flag))
                        except BotBlocked as e:
                            logger.exception(e)

            await bot.send_message(chat_id=uid,
                                   parse_mode='html',
                                   text=all_messages['OFF PUBLIC'][language]\
                                        .format(all_keyboards['PUBLIC CHATS KEYBOARD']\
                                                             [f'{chat_name.upper()} BUTTON']\
                                                             ['NAME'][language].rstrip()))
            await db.update_many(table_name='users',
                                 items={'status': 'in_menu', 'in_chat': None},
                                 condition={'tg_id': uid})

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