from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton as Button
from tools.messages import all_keyboards, all_messages
from tools.logger import get_logger

logger = get_logger('main.keyboards.inline.py')

class Keyboard():
    def __init__(self):
        self.languages = ['UA', 'RU', 'EN']
        self.flags = {
            'UA': '🇺🇦 Українська 🇺🇦',
            'RU': '🇷🇺 Русский 🇷🇺',
            'EN': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 English 🏴󠁧󠁢󠁥󠁮󠁧󠁿',
        }
        self.keyboards = {key:{}.fromkeys(self.languages) for key in all_keyboards.keys()}
        self.load_keyboards()

    def load_keyboards(self, callback_data=None) -> InlineKeyboardMarkup:
        for language in self.languages:
            for keyboard_name, keyboard_data in all_keyboards.items():
                keyboard = InlineKeyboardMarkup(row_width=1)
                for button_data in keyboard_data.values():
                    for data in button_data.values():
                        if callback_data is None:
                            callback_data = data
                            continue
                        keyboard.add(Button(data[language],
                                            callback_data=callback_data))
                        callback_data = None
                    self.keyboards[keyboard_name][language] = keyboard

    def get(self, name: str, language: str) -> InlineKeyboardMarkup:
        keyboard = self.keyboards[name][language]
        logger.debug(f'method kb.get: return keyboard={keyboard}')
        return keyboard

    def get_language_keyboard(self, language: str) -> InlineKeyboardMarkup :
        keyboard = InlineKeyboardMarkup(row_width=1)
        key_back_to_settings = all_keyboards['LANGUAGE SETTINGS KEYBOARD']['BACK TO SETTINGS BUTTON']['NAME'][language]
        languages = self.languages[:]
        languages.remove(language)
        for key_language in languages:
            keyboard.add(Button(self.flags[key_language], callback_data=f'language:{key_language}'))
        keyboard.add(Button(key_back_to_settings, callback_data='settings'))
        logger.debug(f'method kb.get_language_keyboard: return keyboard={keyboard}')
        return keyboard

    def get_public_chats(self, public_chats_data: list, language):
        keyboard = InlineKeyboardMarkup(row_width=1)
        key_back_to_connection = all_keyboards['PUBLIC CHATS KEYBOARD']['BACK TO CONNECTION BUTTON']['NAME'][language]

        for chat_name, chat_code, members_online in public_chats_data:
            text = all_keyboards['PUBLIC CHATS KEYBOARD'][f'{chat_name.upper()} BUTTON']['NAME'][language] +\
                   all_messages['MEMBERS COUNT'][language].format(members_online)
            keyboard.add(Button(text, callback_data=f'join_public:{chat_code}'))
        keyboard.add(Button(key_back_to_connection, callback_data='connect'))
        logger.debug(f'method kb.get_public_chats: return keyboard={keyboard}')
        return keyboard