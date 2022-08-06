from string import ascii_lowercase, digits, punctuation

cyrillic_lowercase = 'абвгдежзийклмнопрстуфхцчшщъыьэюяёєії'
all_symbols = ascii_lowercase + cyrillic_lowercase + digits + punctuation + ' '

all_buttons = {
    'MENU': {
        'CONNECT': {
            'UA': 'Підключитись',
            'RU': 'Подключиться',
            'EN': 'Connect',
        },
        'CREATE': {
            'UA': 'Створити',
            'RU': 'Создать',
            'EN': 'Create',
        },
        'SETTINGS': {
            'UA': 'Налаштування',
            'RU': 'Настройки',
            'EN': 'Settings',
        },
    },
    'CONNECT': {
        'PUBLIC CHATS': {
            'UA': 'Публічні чати',
            'RU': 'Публичные чаты',
            'EN': 'Public chats',
        },
        'PRIVATE CHATS': {
            'UA': 'Приватні чати',
            'RU': 'Приватные чаты',
            'EN': 'Private chats',
        }
    },
    'CREATE': {
        'OPEN CHAT': {
            'UA': 'Відкритий чат',
            'RU': 'Открытый чат',
            'EN': 'Open chat',
        },
        'SECRET CHAT': {
            'UA': 'Секретний чат',
            'RU': 'Секретный чат',
            'EN': 'Secret chat',
        }
    },
    'SETTINGS': {
        'NICKNAME': {
            'UA': 'Нікнейм',
            'RU': 'Никнейм',
            'EN': 'Nickname',
        },
        'LANGUAGE': {
            'UA': 'Мова',
            'RU': 'Язык',
            'EN': 'Language',
        },
        'FLAG': {
            'UA': 'Прапор',
            'RU': 'Флаг',
            'EN': 'Flag',
        },
    },

    'BACK TO MENU': {
            'UA': '⬅️Повернутись до меню',
            'RU': '⬅️Вернуться в меню',
            'EN': '⬅️Return to menu',
    },
    'BACK TO CONNECT': {
            'UA': '⬅️Повернутись назад',
            'RU': '⬅️Вернуться назад',
            'EN': '⬅️Return back',
    },
    'BACK TO CREATE': {
            'UA': '⬅️Повернутись назад',
            'RU': '⬅️Вернуться назад',
            'EN': '⬅️Return back',
    },
    'BACK TO SETTINGS': {
            'UA': '⬅️Повернутись назад',
            'RU': '⬅️Вернуться назад',
            'EN': '⬅️Return back',
    },
}

all_messages = {
    'NICKNAME': {
        'CREATE NICKNAME': {
            'UA': 'Щоб почати користуватися ботом, придумай собі нікнейм:',
            'RU': 'Чтобы начать пользоваться ботом, придумай себе никнейм:',
            'EN': 'To start using the bot, create a nickname:',
        },
        'NICKNAME SAVED': {
            'UA': 'Новий нікнейм збережено:\n{}',
            'RU': 'Сохранен новый никнейм:\n{}',
            'EN': 'New nickname saved:\n{}',
        },
        'TOO LONG NICKNAME': {
            'UA': 'Нікнейм не повинен перевищувати 16 символів.\nВведіть нікнейм ще раз:',
            'RU': 'Никнейм не должен превышать 16 символов.\nВведите никнейм еще раз:',
            'EN': 'Your nickname must be 1-16 characters.\nEnter your nickname again:',
        },
        'WRONG SYMBOLS IN NICKNAME': {
            'UA': 'Нікнейм повинен складатися лише з латиниці, кирилиці та знаків пунктуації.\nВведіть нікнейм ще раз:',
            'RU': 'Никнейм должен состоять только из латиницы, кириллицы и знаков пунктуации.\nВведите никнейм еще раз:',
            'EN': 'The nickname should consist only of latin, cyrillic and punctuation marks..\nEnter your nickname again:',
        },
        'NOT UNIQUE NICKNAME': {
            'UA': 'Цей нікнейм вже зайнятий.\nВведіть нікнейм ще раз:',
            'RU': 'Этот никнейм уже занят.\nВведите никнейм еще раз:',
            'EN': 'This nickname is already taken.\nEnter your nickname again:',
        },
    },
    'MENU': {
        'UA': 'Головне меню',
        'RU': 'Главное меню',
        'EN': 'Main menu',
    },
    'CONNECT': {
        'UA': 'Підключитись',
        'RU': 'Подключиться',
        'EN': 'Connect',
    },
    'CONNECT PUBLIC': {
        'UA': 'Список чатів за темами.',
        'RU': 'Список чатов по тематикам.',
        'EN': 'List of chats by topic',
    },
    'CONNECT PRIVATE': {
        'UA': 'Список чатів за темами.',
        'RU': 'Список чатов по тематикам.',
        'EN': 'List of chats by topic',
    },
    'CREATE': {
        'UA': 'Створити',
        'RU': 'Создать',
        'EN': 'Create',
    },
    'CREATE CHAT': {
        'UA': 'Створити чат',
        'RU': 'Создать чат',
        'EN': 'Create chat',
    },
    'SETTINGS': {
        'UA': 'Налаштування профілу',
        'RU': 'Настройка профиля',
        'EN': 'Profile setup',
    },
    'EDIT NICKNAME': {
        'UA': 'Редагування нікнейму',
        'RU': 'Редактирование никнейма',
        'EN': 'Nickname editing',
    },
    'EDIT LANGUAGE': {
        'UA': 'Редагування мови',
        'RU': 'Редактирование языка',
        'EN': 'Language editing',
    },
    'EDIT FLAG': {
        'UA': 'Редагування прапору',
        'RU': 'Редактирование флага',
        'EN': 'Flag editing',
    },



    "MAIN MENU": "WELCOME TO ANONYMOUS CHATS\n\nYou can create our own chat or join chat if you have invite code.\n\n\nTHERE ARE NO RULES HERE",
    "HOST PRIVATE MENU": "⚠️ It's your private chat.\n\nSomeone who gets your password can connect.\n\nPassword: {}",
    "HOST PUBLIC MENU": "⚠️ It's your public chat.\n\nAnyone can join here.\n\nChat name: *{}*",
    "CONNECT MENU": "⚠️ Write password to enter the private chat:",
    "CREATE PUBLIC CHAT": "⚠️ Write public chat name:"
}
