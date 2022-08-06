from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.exceptions import BotBlocked
from tools.messages import all_messages
from tools.logger import get_logger
from tools.database import db
from tools.bot import bot
from tools.messages import all_messages
import keyboards.inline as kb

async def connect(callback: types.CallbackQuery):
    logger.debug(f'function connect: get "connect" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['CONNECT'][language],
                                reply_markup=kb.get_connect_keyboard(language))


async def connect_public(callback: types.CallbackQuery):
    logger.debug(f'function connect_public: get "connect_public" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['CONNECT PUBLIC'][language],
                                reply_markup=kb.get_public_chats_keyboard(language))


async def connect_private(callback: types.CallbackQuery):
    logger.debug(f'function connect_private: get "connect_private" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['CONNECT PRIVATE'][language],
                                reply_markup=kb.get_private_chats_keyboard(language))


async def create(callback: types.CallbackQuery):
    logger.debug(f'function create: get "create" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['CREATE'][language],
                                reply_markup=kb.get_create_keyboard(language))


async def create_open(callback: types.CallbackQuery):
    logger.debug(f'function create_open: get "create_open" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['CREATE CHAT'][language],
                                reply_markup=kb.get_create_open_chat_keyboard(language))


async def create_secret(callback: types.CallbackQuery):
    logger.debug(f'function create_secret: get "create_secret" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['CREATE CHAT'][language],
                                reply_markup=kb.get_create_secret_chat_keyboard(language))


async def settings(callback: types.CallbackQuery):
    logger.debug(f'function settings: get "settings" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['SETTINGS'][language],
                                reply_markup=kb.get_settings_keyboard(language))

async def nickname(callback: types.CallbackQuery):
    logger.debug(f'function nickname: get "nickname" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['EDIT NICKNAME'][language],
                                reply_markup=kb.get_nickname_keyboard(language))


async def language(callback: types.CallbackQuery):
    logger.debug(f'function language: get "language" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['EDIT LANGUAGE'][language],
                                reply_markup=kb.get_language_keyboard(language))


async def flag(callback: types.CallbackQuery):
    logger.debug(f'function language: get "language" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['EDIT FLAG'][language],
                                reply_markup=kb.get_flag_keyboard(language))


async def back_to_menu(callback: types.CallbackQuery):
    logger.debug(f'function back_to_menu: get "back_to_menu" callback {callback}')
    language = await db.get_language(callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=all_messages['MENU'][language],
                                reply_markup=kb.get_menu_keyboard(language))


def callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(connect_private, lambda callback: callback.data.startswith('connect_private'))
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


logger = get_logger('main.handlers.callbacks.py')