from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton as Button
from tools.messages import all_buttons
from tools.logger import get_logger

def get_menu_keyboard(language: str) -> InlineKeyboardMarkup:
    key_connect = Button(all_buttons['MENU']['CONNECT'][language], callback_data='connect')
    key_create = Button(all_buttons['MENU']['CREATE'][language], callback_data='create')
    key_settings = Button(all_buttons['MENU']['SETTINGS'][language], callback_data='settings')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_connect).add(key_create).add(key_settings)
    logger.debug(f'function get_menu_keyboard: return keyboard={keyboard}')
    return keyboard

def get_connect_keyboard(language: str) -> InlineKeyboardMarkup:
    key_connect_public = Button(all_buttons['CONNECT']['PUBLIC CHATS'][language], callback_data='connect_public')
    key_connect_private = Button(all_buttons['CONNECT']['PRIVATE CHATS'][language], callback_data='connect_private')
    key_back_to_menu = Button(all_buttons['BACK TO MENU'][language], callback_data='back_to_menu')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_connect_public).add(key_connect_private).add(key_back_to_menu)
    logger.debug(f'function get_connect_keyboard: return keyboard={keyboard}')
    return keyboard

def get_public_chats_keyboard(language: str) -> InlineKeyboardMarkup:
    key_back_to_connect = Button(all_buttons['BACK TO CONNECT'][language], callback_data='connect')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_back_to_connect)
    logger.debug(f'function get_public_chats_keyboard: return keyboard={keyboard}')
    return keyboard

def get_private_chats_keyboard(language: str) -> InlineKeyboardMarkup:
    key_back_to_connect = Button(all_buttons['BACK TO CONNECT'][language], callback_data='connect')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_back_to_connect)
    logger.debug(f'function get_private_chats_keyboard: return keyboard={keyboard}')
    return keyboard

def get_create_keyboard(language: str) -> InlineKeyboardMarkup:
    key_create_open = Button(all_buttons['CREATE']['OPEN CHAT'][language], callback_data='create_open')
    key_connect_secret = Button(all_buttons['CREATE']['SECRET CHAT'][language], callback_data='create_secret')
    key_back_to_menu = Button(all_buttons['BACK TO MENU'][language], callback_data='back_to_menu')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_create_open).add(key_connect_secret).add(key_back_to_menu)
    logger.debug(f'function get_create_keyboard: return keyboard={keyboard}')
    return keyboard

def get_create_open_chat_keyboard(language: str) -> InlineKeyboardMarkup:
    key_back_to_create = Button(all_buttons['BACK TO CREATE'][language], callback_data='create')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_back_to_create)
    logger.debug(f'function get_create_open_chat_keyboard: return keyboard={keyboard}')
    return keyboard

def get_create_secret_chat_keyboard(language: str) -> InlineKeyboardMarkup:
    key_back_to_create = Button(all_buttons['BACK TO CREATE'][language], callback_data='create')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_back_to_create)
    logger.debug(f'function get_create_secret_chat_keyboard: return keyboard={keyboard}')
    return keyboard

def get_settings_keyboard(language: str) -> InlineKeyboardMarkup:
    key_nickname = Button(all_buttons['SETTINGS']['NICKNAME'][language], callback_data='nickname')
    key_language = Button(all_buttons['SETTINGS']['LANGUAGE'][language], callback_data='language')
    key_flag = Button(all_buttons['SETTINGS']['FLAG'][language], callback_data='flag')
    key_back_to_menu = Button(all_buttons['BACK TO MENU'][language], callback_data='back_to_menu')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_nickname).add(key_language).add(key_flag).add(key_back_to_menu)
    logger.debug(f'function get_settings_keyboard: return keyboard={keyboard}')
    return keyboard

def get_nickname_keyboard(language: str) -> InlineKeyboardMarkup:
    key_back_to_settings = Button(all_buttons['BACK TO SETTINGS'][language], callback_data='settings')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_back_to_settings)
    logger.debug(f'function get_nickname_keyboard: return keyboard={keyboard}')
    return keyboard

def get_language_keyboard(language: str) -> InlineKeyboardMarkup:
    key_back_to_settings = Button(all_buttons['BACK TO SETTINGS'][language], callback_data='settings')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_back_to_settings)
    logger.debug(f'function get_language_keyboard: return keyboard={keyboard}')
    return keyboard

def get_flag_keyboard(language: str) -> InlineKeyboardMarkup:
    key_back_to_settings = Button(all_buttons['BACK TO SETTINGS'][language], callback_data='settings')
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(key_back_to_settings)
    logger.debug(f'function get_flag_keyboard: return keyboard={keyboard}')
    return keyboard


logger = get_logger('main.keyboards.inline.py')