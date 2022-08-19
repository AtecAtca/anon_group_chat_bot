from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import BotBlocked, UserDeactivated
from tools.logger import get_logger
from tools.database import db
from tools.bot import bot
from tools.messages import all_messages, all_flags, all_keyboards
from keyboards.inline import Keyboard
from random import choices


async def connect(callback: types.CallbackQuery):
    logger.debug(f'function connect: get "connect" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['CONNECT'][language],
                                              reply_markup=kb.get('CONNECTION KEYBOARD', language))
    await db.update_many(table_name='users',
                         items={'status': 'in_connect', 'last_activity': bot_message.edit_date},
                         condition={'tg_id': uid})
    await callback.answer()


async def connect_public(callback: types.CallbackQuery):
    logger.debug(f'function connect_public: get "connect_public" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})

    non_active_members_data = [i for i in await db.get_non_active_members_data()]

    if non_active_members_data:
        for afk_member_data in non_active_members_data:
            afk_member_id, afk_member_language = afk_member_data
            chat_members_data = [i for i in await db.get_chat_members(afk_member_id, with_language=True)]
            await db.update_many(table_name='users',
                                 items={'status': 'in_menu', 'in_chat': None},
                                 condition={'tg_id': afk_member_id})
            if chat_members_data:
                nickname, flag = await db.get(table_name='users',
                                              items=('nickname', 'flag'),
                                              condition={'tg_id': afk_member_id})
                flag = '' if flag is None else f'[{flag}]'
                for member_data in chat_members_data:
                    member_uid, member_language = member_data
                    try:
                        await bot.send_message(chat_id=member_uid,
                                               parse_mode='html',
                                               text=all_messages['USER KICKED'][member_language] \
                                               .format(nickname, flag))
                    except (BotBlocked, UserDeactivated) as e:
                        logger.exception(e)
                        await db.update_many(table_name='users',
                                             items={'status': 'bot_blocked', 'in_chat': None},
                                             condition={'tg_id': member_uid})
            try:
                await bot.send_message(afk_member_id, all_messages['KICKED MEMBER'][afk_member_language],
                                       parse_mode='html')
            except (BotBlocked, UserDeactivated) as e:
                logger.exception(e)
                await db.update_many(table_name='users',
                                     items={'status': 'bot_blocked', 'in_chat': None},
                                     condition={'tg_id': afk_member_id})

    public_chats_data = await db.get_public_chats_data()
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['CONNECT PUBLIC'][language],
                                              parse_mode='html',
                                              reply_markup=kb.get_public_chats(
                                                           public_chats_data=public_chats_data,
                                                           language=language))
    await db.update_many(table_name='users',
                         items={'status': 'in_connect_public', 'last_activity': bot_message.edit_date},
                         condition={'tg_id': uid})
    await callback.answer()


async def connect_private(callback: types.CallbackQuery):
    logger.debug(f'function connect_private: get "connect_private" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['CONNECT PRIVATE'][language],
                                              reply_markup=kb.get('PRIVATE CHATS KEYBOARD', language))
    await db.update_many(table_name='users',
                         items={'status': 'in_connect_private', 'last_activity': bot_message.edit_date},
                         condition={'tg_id': uid})
    await callback.answer()


async def create(callback: types.CallbackQuery):
    logger.debug(f'function create: get "create" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['CREATE'][language],
                                              reply_markup=kb.get('CREATION KEYBOARD', language))
    await db.update_many(table_name='users',
                         items={'status': 'in_create', 'last_activity': bot_message.edit_date},
                         condition={'tg_id': uid})
    await callback.answer()


async def create_open(callback: types.CallbackQuery):
    logger.debug(f'function create_open: get "create_open" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['CREATE CHAT'][language],
                                              reply_markup=kb.get('CREATE OPEN CHAT KEYBOARD', language))
    await db.update_many(table_name='users',
                         items={'status': 'in_create_open', 'last_activity': bot_message.edit_date},
                         condition={'tg_id': uid})
    await callback.answer()


async def create_secret(callback: types.CallbackQuery):
    logger.debug(f'function create_secret: get "create_secret" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['CREATE CHAT'][language],
                                              reply_markup=kb.get('CREATE SECRET CHAT KEYBOARD', language))
    await db.update_many(table_name='users',
                         items={'status': 'in_create_secret', 'last_activity': bot_message.edit_date},
                         condition={'tg_id': uid})
    await callback.answer()


async def settings(callback: types.CallbackQuery):
    logger.debug(f'function settings: get "settings" callback {callback}')
    uid = callback.from_user.id
    nickname, language, flag = await db.get(table_name='users',
                                            items=('nickname', 'language', 'flag'),
                                            condition={'tg_id': uid})
    flag = all_messages['NO FLAG'][language] if flag is None else flag
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['SETTINGS'][language]\
                                                   .format(nickname, language, flag),
                                              parse_mode='html',
                                              reply_markup=kb.get('SETTINGS KEYBOARD', language))
    await db.update_many(table_name='users',
                         items={'status': 'in_settings', 'last_activity': bot_message.edit_date},
                         condition={'tg_id': uid})
    await callback.answer()


async def nickname(callback: types.CallbackQuery):
    logger.debug(f'function nickname: get "nickname" callback {callback}')
    uid = callback.from_user.id
    language, nickname = await db.get(table_name='users',
                                      items=('language', 'nickname'),
                                      condition={'tg_id': uid})
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['EDIT NICKNAME'][language].format(nickname),
                                              parse_mode='html',
                                              reply_markup=kb.get('NICKNAME SETTINGS KEYBOARD', language))
    await db.update_many(table_name='users',
                         items={'status': 'in_set_nickname', 'last_activity': bot_message.edit_date},
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
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['EDIT LANGUAGE'][language]\
                                                   .format((kb.flags[language]).replace(' ', '')),
                                              parse_mode='html',
                                              reply_markup=kb.get_language_keyboard(language))
    await db.update_many(table_name='users',
                         items={'status': 'in_set_language', 'last_activity': bot_message.edit_date},
                         condition={'tg_id': uid})
    await callback.answer()


async def flag(callback: types.CallbackQuery):
    logger.debug(f'function language: get "language" callback {callback}')
    uid = callback.from_user.id
    language, flag = await db.get(table_name='users',
                                  items=('language', 'flag'),
                                  condition={'tg_id': uid})
    flag = all_messages['NO FLAG'][language] if flag is None else flag
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['EDIT FLAG'][language] \
                                                   .format(flag, *choices(all_flags, k=3)),
                                              parse_mode='html',
                                              reply_markup=kb.get('FLAG SETTINGS KEYBOARD', language))
    await db.update_many(table_name='users',
                         items={'status': 'in_set_flag', 'last_activity': bot_message.edit_date},
                         condition={'tg_id': uid})
    await callback.answer()


async def back_to_menu(callback: types.CallbackQuery):
    logger.debug(f'function back_to_menu: get "back_to_menu" callback {callback}')
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['MENU'][language],
                                              parse_mode='html',
                                              reply_markup=kb.get('MENU KEYBOARD', language))
    await db.update_many(table_name='users',
                         items={'status': 'in_menu', 'last_activity': bot_message.edit_date},
                         condition={'tg_id': uid})
    await callback.answer()


async def join_public(callback: types.CallbackQuery):
    logger.debug(f'function join_public: get "join" callback {callback}')
    chat_code = str(callback.data.split(':')[1])
    uid = callback.from_user.id
    language = await db.get(table_name='users',
                            items=('language',),
                            condition={'tg_id': uid})
    await db.update_many(table_name='users',
                         items={'status': 'in_public_chat', 'in_chat': chat_code},
                         condition={'tg_id': uid})
    chat_name = await db.get_chat_name(uid)
    chat_members_data = [i for i in await db.get_chat_members(uid, with_language=True)]
    bot_message = await bot.edit_message_text(chat_id=uid,
                                              message_id=callback.message.message_id,
                                              text=all_messages['ON PUBLIC'][language] \
                                                   .format(all_keyboards['PUBLIC CHATS KEYBOARD'] \
                                                                        [f'{chat_name.upper()} BUTTON'] \
                                                                        ['NAME'][language].replace(' ', ''),
                                                           len(chat_members_data)+1),
                                              parse_mode='html')
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
                                       text=all_messages['USER CONNECT'][member_language] \
                                       .format(nickname, flag))
            except BotBlocked as e:
                logger.exception(e)
                await db.update_many(table_name='users',
                                     items={'status': 'bot_blocked', 'in_chat': None},
                                     condition={'tg_id': member_uid})
    await db.update(table_name='users',
                    items={'last_activity': bot_message.edit_date},
                    condition={'tg_id': uid})
    await callback.answer()


def callback_handlers(dp: Dispatcher):
    for func_name, func_obj in all_callback_funcs.items():
        dp.register_callback_query_handler(func_obj, Text(startswith=func_name))


kb = Keyboard()
all_callback_funcs = {name: obj for (name, obj) in sorted(vars().items(),
                                                          key=lambda x: len(x[0]),
                                                          reverse=True)\
                      if hasattr(obj, "__class__")
                      and obj.__class__.__name__ == "function"
                      and name not in ('get_logger', 'callback_handlers')}

logger = get_logger('main.handlers.callbacks.py')
