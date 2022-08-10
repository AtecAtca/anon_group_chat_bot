from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import BotBlocked
from tools.logger import get_logger
from tools.database import db
from tools.bot import bot
from tools.messages import all_messages, all_flags, all_keyboards
from keyboards.inline import Keyboard
from random import choices

kb = Keyboard()

async def connect(callback: types.CallbackQuery):
    logger.debug(f'function connect: get "connect" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['CONNECT'][language],
                                reply_markup=kb.get('CONNECTION KEYBOARD',language))
    await db.update(table_name='users',
                    items={'status': 'in_connect'},
                    condition={'tg_id': uid})
    await callback.answer()

async def connect_public(callback: types.CallbackQuery):
    logger.debug(f'function connect_public: get "connect_public" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['CONNECT PUBLIC'][language],
                                reply_markup=kb.get_public_chats(
                                    public_chats=await db.get(table_name='chats',
                                                              items=('chat_name', 'chat_code', 'chat_members'),
                                                              condition={'chat_type': 'public'},
                                                              order_by={'chat_members': 'DESC'},
                                                              fetchall=True),
                                    language=language))
    await db.update(table_name='users',
                    items={'status': 'in_connect_public'},
                    condition={'tg_id': uid})
    await callback.answer()

async def connect_private(callback: types.CallbackQuery):
    logger.debug(f'function connect_private: get "connect_private" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['CONNECT PRIVATE'][language],
                                reply_markup=kb.get('PRIVATE CHATS KEYBOARD',language))
    await db.update(table_name='users',
                    items={'status': 'in_connect_private'},
                    condition={'tg_id': uid})
    await callback.answer()

async def create(callback: types.CallbackQuery):
    logger.debug(f'function create: get "create" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['CREATE'][language],
                                reply_markup=kb.get('CREATION KEYBOARD',language))
    await db.update(table_name='users',
                    items={'status': 'in_create'},
                    condition={'tg_id': uid})
    await callback.answer()

async def create_open(callback: types.CallbackQuery):
    logger.debug(f'function create_open: get "create_open" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['CREATE CHAT'][language],
                                reply_markup=kb.get('CREATE OPEN CHAT KEYBOARD',language))
    await db.update(table_name='users',
                    items={'status': 'in_create_open'},
                    condition={'tg_id': uid})
    await callback.answer()

async def create_secret(callback: types.CallbackQuery):
    logger.debug(f'function create_secret: get "create_secret" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['CREATE CHAT'][language],
                                reply_markup=kb.get('CREATE SECRET CHAT KEYBOARD',language))
    await db.update(table_name='users',
                    items={'status': 'in_create_secret'},
                    condition={'tg_id': uid})
    await callback.answer()

async def settings(callback: types.CallbackQuery):
    logger.debug(f'function settings: get "settings" callback {callback}')
    uid = callback.from_user.id
    nickname, language, flag = await db.get(table_name='users',
                                            items=('nickname', 'language', 'flag'),
                                            condition={'tg_id': uid})
    if flag is None:
        flag = all_messages['NO FLAG'][language]
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['SETTINGS'][language].format(nickname, language, flag),
                                parse_mode='html',
                                reply_markup=kb.get('SETTINGS KEYBOARD', language))
    await db.update(table_name='users',
                    items={'status': 'in_settings'},
                    condition={'tg_id': uid})
    await callback.answer()

async def nickname(callback: types.CallbackQuery):
    logger.debug(f'function nickname: get "nickname" callback {callback}')
    uid = callback.from_user.id
    language, nickname = await db.get(table_name='users',
                                      items=('language', 'nickname'),
                                      condition={'tg_id': uid})
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['EDIT NICKNAME'][language].format(nickname),
                                parse_mode='html',
                                reply_markup=kb.get('NICKNAME SETTINGS KEYBOARD', language))
    await db.update(table_name='users',
                    items={'status': 'in_set_nickname'},
                    condition={'tg_id': uid})
    await callback.answer()

async def language(callback: types.CallbackQuery):
    logger.debug(f'function language: get "language" callback {callback}')
    uid = callback.from_user.id
    callback_data = callback.data.split(':')
    if len(callback_data) == 2:
        language = callback_data[1]
        await db.update(table_name='users',
                        items={'language': language},
                        condition={'tg_id': uid})
    else:
        language = await db.get(table_name='users',
                                items=('language',),
                                condition={'tg_id': uid})
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['EDIT LANGUAGE'][language].format(kb.flags[language]),
                                parse_mode='html',
                                reply_markup=kb.get_language_keyboard(language))
    await db.update(table_name='users',
                    items={'status': 'in_set_language'},
                    condition={'tg_id': uid})
    await callback.answer()

async def flag(callback: types.CallbackQuery):
    logger.debug(f'function language: get "language" callback {callback}')
    uid = callback.from_user.id
    language, flag = await db.get(table_name='users',
                                 items=('language', 'flag'),
                                 condition={'tg_id': uid})
    if flag is None:
        flag = all_messages['NO FLAG'][language]
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['EDIT FLAG'][language]\
                                     .format(flag ,*choices(all_flags, k=3)),
                                parse_mode='html',
                                reply_markup=kb.get('FLAG SETTINGS KEYBOARD', language))
    await db.update(table_name='users',
                    items={'status': 'in_set_flag'},
                    condition={'tg_id': uid})
    await callback.answer()




async def back_to_menu(callback: types.CallbackQuery):
    logger.debug(f'function back_to_menu: get "back_to_menu" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['MENU'][language],
                                reply_markup=kb.get('MENU KEYBOARD',language))
    await db.update(table_name='users',
                    items={'status': 'in_menu'},
                    condition={'tg_id': uid})
    await callback.answer()





async def join_public(callback: types.CallbackQuery):
    logger.debug(f'function join_public: get "join" callback {callback}')
    chat_code = str(callback.data.split(':')[1])
    uid = callback.from_user.id
    language, nickname, flag = await db.get(table_name='users',
                                            items=('language','nickname', 'flag'),
                                            condition={'tg_id': uid})
    await db.update(table_name='chats',
                    items={'chat_members': uid},
                    array_func='array_append',
                    condition={'chat_code': chat_code})
    chat_name, chat_members = await db.get(table_name='chats',
                                          items=('chat_name', 'chat_members'),
                                          condition={'chat_code': chat_code})
    await bot.edit_message_text(chat_id=uid,
                                message_id=callback.message.message_id,
                                text=all_messages['ON PUBLIC'][language]\
                                     .format(all_keyboards['PUBLIC CHATS KEYBOARD']\
                                                          [f'{chat_name.upper()} BUTTON']\
                                                          ['NAME'][language].rstrip(),
                                            len(chat_members)),
                                parse_mode='html')
    await db.update_many(table_name='users',
                         items={'status': 'in_public_chat', 'in_chat': chat_code},
                         condition={'tg_id': uid})
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
                                           text=all_messages['USER CONNECT'][member_language]\
                                                .format(nickname, flag))
                except BotBlocked as e:
                    logger.exception(e)
    await callback.answer()

#Text(startswith='connect_private')

def callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(connect_private, Text(startswith='connect_private'))
    dp.register_callback_query_handler(connect_public, lambda callback: callback.data.startswith('connect_public'))
    dp.register_callback_query_handler(connect, lambda callback: callback.data.startswith('connect'))
    dp.register_callback_query_handler(create_secret, lambda callback: callback.data.startswith('create_secret'))
    dp.register_callback_query_handler(create_open, lambda callback: callback.data.startswith('create_open'))
    dp.register_callback_query_handler(create, lambda callback: callback.data.startswith('create'))
    dp.register_callback_query_handler(settings, lambda callback: callback.data.startswith('settings'))
    dp.register_callback_query_handler(back_to_menu, lambda callback: callback.data.startswith('back_to_menu'))
    dp.register_callback_query_handler(nickname, lambda callback: callback.data.startswith('nickname'))
    dp.register_callback_query_handler(language, lambda callback: callback.data.startswith('language'))
    dp.register_callback_query_handler(flag, lambda callback: callback.data.startswith('flag'))
    dp.register_callback_query_handler(join_public, lambda callback: callback.data.startswith('join'))




logger = get_logger('main.handlers.callbacks.py')