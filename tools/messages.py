from string import ascii_lowercase, digits, punctuation

cyrillic_lowercase = 'абвгдежзийклмнопрстуфхцчшщъыьэюяёєії'
all_symbols = ascii_lowercase + cyrillic_lowercase + digits + punctuation + ' '



default = {
    'language': 'RU'
}

all_keyboards = {
    'MENU KEYBOARD': {
        'CONNECT BUTTON': {
            'CALLBACK DATA': 'connect',
            'NAME': {
                'UA': 'Підключитись',
                'RU': 'Подключиться',
                'EN': 'Connect',
            }
        },
        'CREATE BUTTON': {
            'CALLBACK DATA': 'create',
            'NAME': {
                'UA': 'Створити',
                'RU': 'Создать',
                'EN': 'Create',
            }
        },
        'SETTINGS BUTTON': {
            'CALLBACK DATA': 'settings',
            'NAME': {
                'UA': 'Налаштування',
                'RU': 'Настройки',
                'EN': 'Settings',
            }
        },
    },
    'CONNECTION KEYBOARD': {
        'PUBLIC CHATS BUTTON': {
            'CALLBACK DATA': 'connect_public',
            'NAME': {
                'UA': 'Публічні чати',
                'RU': 'Публичные чаты',
                'EN': 'Public chats',
            }
        },
        'PRIVATE CHATS': {
            'CALLBACK DATA': 'connect_private',
            'NAME': {
                'UA': 'Приватні чати',
                'RU': 'Приватные чаты',
                'EN': 'Private chats',
            }
        },
        'BACK TO MENU BUTTON': {
            'CALLBACK DATA': 'back_to_menu',
            'NAME': {
                'UA': '⬅️Повернутись до меню',
                'RU': '⬅️Вернуться в меню',
                'EN': '⬅️Return to menu',
            }
        },
    },
    'CREATION KEYBOARD': {
        'OPEN CHAT BUTTON': {
            'CALLBACK DATA': 'create_open',
            'NAME': {
                'UA': 'Відкритий чат',
                'RU': 'Открытый чат',
                'EN': 'Open chat',
            }
        },
        'SECRET CHAT BUTTON': {
            'CALLBACK DATA': 'create_secret',
            'NAME': {
                'UA': 'Секретний чат',
                'RU': 'Секретный чат',
                'EN': 'Secret chat',
            }
        },
        'BACK TO MENU BUTTON': {
            'CALLBACK DATA': 'back_to_menu',
            'NAME': {
                'UA': '⬅️Повернутись до меню',
                'RU': '⬅️Вернуться в меню',
                'EN': '⬅️Return to menu',
            }
        },
    },
    'SETTINGS KEYBOARD': {
        'NICKNAME BUTTON': {
            'CALLBACK DATA': 'nickname',
            'NAME': {
                'UA': '😎 Нікнейм 😎',
                'RU': '😎 Никнейм 😎',
                'EN': '😎 Nickname 😎',
            }
        },
        'LANGUAGE BUTTON': {
            'CALLBACK DATA': 'language',
            'NAME': {
                'UA': '💬 Мова 💬',
                'RU': '💬 Язык 💬',
                'EN': '💬 Language 💬',
            }
        },
        'FLAG BUTTON': {
            'CALLBACK DATA': 'flag',
            'NAME': {
                'UA': '🏳️ Прапор 🏳️',
                'RU': '🏳️ Флаг 🏳️',
                'EN': '🏳️ Flag 🏳️',
            }
        },
        'BACK TO MENU BUTTON': {
            'CALLBACK DATA': 'back_to_menu',
            'NAME': {
                'UA': '⬅️ Повернутись до меню',
                'RU': '⬅️ Вернуться в меню',
                'EN': '⬅️ Return to menu',
            }
        },
    },

    'PUBLIC CHATS KEYBOARD': {
        'MEMES BUTTON': {
            'CALLBACK DATA': '0000',
            'NAME': {
                'UA': '🤡 Меми      ️ ️',
                'RU': '🤡 Мемы  ️ ️️ ️ ️     ️ ️️ ️ ️ ',
                'EN': '🤡 Memes',
            }
        },
        'GAMES BUTTON': {
            'CALLBACK DATA': '1111',
            'NAME': {
                'UA': '🎮 Ігри          ️ ️',
                'RU': '🎮 Игры    ️ ️️ ️ ️     ️ ️️ ️ ️ ',
                'EN': '🎮 Games',
            }
        },
        'MUSIC BUTTON': {
            'CALLBACK DATA': '2222',
            'NAME': {
                'UA': '🎧 Музика   ️ ️',
                'RU': '🎧 Музыка️️ ️ ️     ️ ️️ ️ ️ ',
                'EN': '🎧 Music ',
            }
        },
        'FILMS BUTTON': {
            'CALLBACK DATA': '3333',
            'NAME': {
                'UA': '🎬 Кіно          ️ ️',
                'RU': '🎬 Кино     ️ ️️ ️ ️     ️ ️️ ️ ️ ',
                'EN': '🎬 Films  ',
            }
        },
        'ANIME BUTTON': {
            'CALLBACK DATA': '4444',
            'NAME': {
                'UA': '💩 Аніме ️ ️     ️ ️',
                'RU': '💩 Аниме  ️ ️️ ️ ️     ️ ️️ ️ ️ ',
                'EN': '💩 Anime',
            }
        },
        'BOOKS BUTTON': {
            'CALLBACK DATA': '5555',
            'NAME': {
                'UA': '📖 Книги    ️ ️️ ️ ️ ',
                'RU': '📖 Книги   ️ ️️ ️ ️     ️ ️️ ️ ️ ',
                'EN': '📖 Books',
            }
        },
        'TRAVEL BUTTON': {
            'CALLBACK DATA': '6666',
            'NAME': {
                'UA': '🗺 Подорожі',
                'RU': '🗺 Путешествия',
                'EN': '🗺 Travel',
            }
        },
        'BACK TO CONNECTION BUTTON': {
            'CALLBACK DATA': 'connect',
            'NAME': {
                'UA': '⬅️ Повернутись назад',
                'RU': '⬅️ Вернуться назад',
                'EN': '⬅️ Return back',
            }
        },
    },
    'PRIVATE CHATS KEYBOARD': {
        'BACK TO CONNECTION BUTTON': {
            'CALLBACK DATA': 'connect',
            'NAME': {
                'UA': '⬅️ Повернутись назад',
                'RU': '⬅️ Вернуться назад',
                'EN': '⬅️ Return back',
            }
        },
    },
    'CREATE OPEN CHAT KEYBOARD': {
        'BACK TO CREATION BUTTON': {
            'CALLBACK DATA': 'create',
            'NAME': {
                'UA': '⬅️ Повернутись назад',
                'RU': '⬅️ Вернуться назад',
                'EN': '⬅️ Return back',
            }
        },
    },
    'CREATE SECRET CHAT KEYBOARD': {
        'BACK TO CREATION BUTTON': {
            'CALLBACK DATA': 'create',
            'NAME': {
                'UA': '⬅️ Повернутись назад',
                'RU': '⬅️ Вернуться назад',
                'EN': '⬅️ Return back',
            }
        },
    },
    'NICKNAME SETTINGS KEYBOARD': {
        'BACK TO SETTINGS BUTTON': {
            'CALLBACK DATA': 'settings',
            'NAME': {
                'UA': '⬅️ Повернутись назад',
                'RU': '⬅️ Вернуться назад',
                'EN': '⬅️ Return back',
            }
        },
    },
    'FLAG SETTINGS KEYBOARD': {
        'BACK TO SETTINGS BUTTON': {
            'CALLBACK DATA': 'settings',
            'NAME': {
                'UA': '⬅️ Повернутись назад',
                'RU': '⬅️ Вернуться назад',
                'EN': '⬅️ Return back',
            }
        },
    },
    'LANGUAGE SETTINGS KEYBOARD': {
        'BACK TO SETTINGS BUTTON': {
            'CALLBACK DATA': 'settings',
            'NAME': {
                'UA': '⬅️ Повернутись назад',
                'RU': '⬅️ Вернуться назад',
                'EN': '⬅️ Return back',
            }
        },
    },
}






all_messages = {
    'NICKNAME': {
        'CREATE NICKNAME': {
            'UA': '⚠️ Щоб почати користуватися ботом, придумай собі нікнейм:',
            'RU': '⚠️ Чтобы начать пользоваться ботом, придумай себе никнейм:',
            'EN': '⚠️ To start using the bot, create a nickname:',
        },
        'NICKNAME SAVED': {
            'UA': '💾 Новий нікнейм збережено:\n<code>{}</code>',
            'RU': '💾 Сохранен новый никнейм:\n<code>{}</code>',
            'EN': '💾 New nickname saved:\n<code>{}</code>',
        },
        'TOO LONG NICKNAME': {
            'UA': '⚠️ Нікнейм не повинен перевищувати 16 символів.\nВведіть нікнейм ще раз:',
            'RU': '⚠️ Никнейм не должен превышать 16 символов.\nВведите никнейм еще раз:',
            'EN': '⚠️ Your nickname must be 1-16 characters.\nEnter your nickname again:',
        },
        'WRONG SYMBOLS IN NICKNAME': {
            'UA': '⚠️ Нікнейм повинен складатися лише з латиниці, кирилиці та знаків пунктуації.\nВведіть нікнейм ще раз:',
            'RU': '⚠️ Никнейм должен состоять только из латиницы, кириллицы и знаков пунктуации.\nВведите никнейм еще раз:',
            'EN': '⚠️ The nickname should consist only of latin, cyrillic and punctuation marks..\nEnter your nickname again:',
        },
        'NOT UNIQUE NICKNAME': {
            'UA': '⚠️ Цей нікнейм вже зайнятий.\nВведіть нікнейм ще раз:',
            'RU': '⚠️ Этот никнейм уже занят.\nВведите никнейм еще раз:',
            'EN': '⚠️ This nickname is already taken.\nEnter your nickname again:',
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
    'USER CONNECT': {
        'UA': '<b>🟢 До чату приєднався:</b>\n<code>{}{}</code>',
        'RU': '<b>🟢 К чату присоединился:</b>\n<code>{}{}</code>',
        'EN': '<b>🟢 Joined the chat:</b>\n<code>{}{}</code>',
    },
    'USER DISCONNECT': {
        'UA': '<b>🔴 Вийшов з чату:</b>\n<code>{}{}</code>',
        'RU': '<b>🔴 Вышел с чата:</b>\n<code>{}{}</code>',
        'EN': '<b>🔴 Left the chat:</b>\n<code>{}{}</code>',
    },
    'CONNECT PUBLIC': {
        'UA': 'Список чатів за темами.',
        'RU': 'Список чатов по тематикам.',
        'EN': 'List of chats by topic',
    },
    'ON PUBLIC': {
        'UA': '<b>🟢 Ви підключені:</b>\nЧат: <code>{}</code>\nОнлайн: <code>[ {} ]</code>',
        'RU': '<b>🟢 Вы подключены:</b>\nЧат: <code>{}</code>\nОнлайн: <code>[ {} ]</code>',
        'EN': "<b>🟢 You're connected:</b>\nChat: <code>{}</code>\nOnline: <code>[ {} ]</code>",
    },
    'OFF PUBLIC': {
        'UA': '<b>🔴 Ви відключені:</b>\nЧат: <code>{}</code>',
        'RU': '<b>🔴 Вы отключены:</b>\nЧат: <code>{}</code>',
        'EN': "<b>🔴 You're disconnected:</b>\nChat: <code>{}</code>",
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
        'UA': '<b>Ваш профіль:</b>\nНікнейм: <code>{}</code>\nМова: <code>{}</code>\nПрапор: <code>{}</code>\n\n<i>Виберіть параметри, які ви бажаєте змінити:</i>',
        'RU': '<b>Ваш профиль:</b>\nНикнейм: <code>{}</code>\nЯзык: <code>{}</code>\nФлаг: <code>{}</code>\n\n<i>Выберите настройки, которые вы бы хотели изменить:</i>',
        'EN': '<b>Your profile:</b>\nNickname: <code>{}</code>\nLanguage: <code>{}</code>\nFlag: <code>{}</code>\n\n<i>Select the settings you would like to change:</i>'
    },
    'EDIT NICKNAME': {
        'UA': '😎 <b>Поточний нікнейм:</b> <code>{}</code>\n<i>Надішли мені в чат свій новий нікнейм і я його збережу:</i>',
        'RU': '😎 <b>Текущий никнейм:</b> <code>{}</code>\n<i>Отправь мне в чат свой новый никнейм и я его сохраню:</i>',
        'EN': "😎 <b>Current nickname:</b> <code>{}</code>\n<i>Send me your new nickname in the chat and i'll save it:</i>",
    },
    'EDIT LANGUAGE': {
        'UA': '💬  <b>Поточна мова:</b> <code>{}</code>\n<i>Виберіть мову, яку ви бажаєте використовувати:</i>',
        'RU': '💬  <b>Текущий язык:</b> <code>{}</code>\n<i>Выберите язык, который вы хотели бы использовать:</i>',
        'EN': '💬  <b>Current language:</b> <code>{}</code>\n<i>Select the language you would like to use:</i>',
    },
    'EDIT FLAG': {
        'UA': '🏳️ <b>Поточний прапор:</b> <code>{}</code>\n<i>Надішли мені в чат свій прапор і я його збережу.</i>\n\n<b>Можна додати:</b>\n<code>{}{}{}(прямокутний прапор)</code>\n\n❌<s>Не підходить</s>❌\n<code>🚩🏴‍☠️🎌🇳🇵🇻🇦🇨🇭🏴🏳️🏁</code>',
        'RU': '🏳️ <b>Текущий флаг:</b> <code>{}</code>\n<i>Отправь мне в чат свой флаг и я его сохраню.</i>\n\n<b>Можно добавить:</b>\n<code>{}{}{}(прямоугольный флаг)</code>\n\n❌<s>Не подходит</s>❌\n<code>🚩🏴‍☠️🎌🇳🇵🇻🇦🇨🇭🏴🏳️🏁</code>',
        'EN': "🏳️ <b>Current flag:</b> <code>{}</code>\n<i>Send me your flag in the chat and i'll save it.</i>\n\n<b>Can add:</b>\n<code>{}{}{}(rectangular flag)</code>\n\n❌<s>Unsuitable</s>❌\n<code>🚩🏴‍☠️🎌🇳🇵🇻🇦🇨🇭🏴🏳️🏁</code>",
    },
    'NO FLAG': {
        'UA': '[<i>прапор відсутній</i>]',
        'RU': '[<i>флаг не выбран</i>]',
        'EN': '[<i>no flag</i>]',
    },
    'FLAG SAVED': {
        'UA': '💾 Новий прапор збережено: <code>{}</code>',
        'RU': '💾 Сохранен новый флаг: <code>{}</code>',
        'EN': '💾 New flag saved: <code>{}</code>',
    },
    'WRONG FLAG': {
        'UA': '⚠️ Помилка вводу або цей прапор не підходить!\nВведіть прапор ще раз:',
        'RU': '⚠️ Ошибка ввода или этот флаг не поддерживается!\nВведите флаг еще раз:',
        'EN': '⚠️ An input error or this flag is not supported!\nEnter your flag again:',
    },
    'MEMBERS COUNT': {
        'UA': ' | 👤 Онлайн: [ {} ]',
        'RU': ' | 👤 Онлайн: [ {} ]',
        'EN': ' | 👤 Online: [ {} ]',
    },



    "MAIN MENU": "WELCOME TO ANONYMOUS CHATS\n\nYou can create our own chat or join chat if you have invite code.\n\n\nTHERE ARE NO RULES HERE",
    "HOST PRIVATE MENU": "⚠️ It's your private chat.\n\nSomeone who gets your password can connect.\n\nPassword: {}",
    "HOST PUBLIC MENU": "⚠️ It's your public chat.\n\nAnyone can join here.\n\nChat name: *{}*",
    "CONNECT MENU": "⚠️ Write password to enter the private chat:",
    "CREATE PUBLIC CHAT": "⚠️ Write public chat name:"
}


all_status = ['without_nickname',
            'in_menu', 'in_connect', 'in_connect_public', 'in_connect_private',
            'in_create', 'in_create_open', 'in_create_secret',
            'in_settings', 'in_set_nickname', 'in_set_language', 'in_set_flag']

#max item len = 7
all_flags = ["🇿🇼", "🇿🇲", "🇾🇪", "🇪🇭", "🇼🇫", "🇺🇾", "🇻🇮", "🇺🇿", "🇻🇺", "🇻🇪", "🇻🇳", "🇺🇸", "🏴󠁧󠁢󠁷󠁬󠁳󠁿", "🏴󠁧󠁢󠁳󠁣󠁴󠁿", "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "🇬🇧", "🇦🇪", "🇺🇦", "🇹🇹",
             "🇹🇳", "🇹🇷", "🇹🇲", "🇹🇨", "🇹🇻", "🇺🇬", "🇹🇴", "🇹🇰", "🇹🇬", "🇹🇱", "🇹🇭", "🇹🇿", "🇹🇯", "🇻🇨", "🇸🇩", "🇸🇷", "🇸🇪", "🇸🇾", "🇹🇼",
             "🇵🇲", "🇱🇨", "🇰🇳", "🇸🇭", "🇧🇱", "🇱🇰", "🇪🇸", "🇸🇮", "🇬🇸", "🇸🇧", "🇸🇴", "🇿🇦", "🇰🇷", "🇸🇸", "🇸🇰", "🇸🇽", "🇸🇬", "🇸🇱", "🇸🇨",
             "🇷🇸", "🇸🇳", "🇷🇴", "🇷🇺", "🇷🇼", "🇼🇸", "🇸🇲", "🇸🇹", "🇸🇦", "🇷🇪", "🇶🇦", "🇵🇷", "🇵🇹", "🇵🇱", "🇵🇳", "🇵🇭", "🇵🇰", "🇵🇼", "🇵🇸",
             "🇵🇦", "🇵🇬", "🇵🇾", "🇵🇪", "🇴🇲", "🇳🇴", "🇲🇵", "🇲🇰", "🇰🇵", "🇳🇫", "🇳🇺", "🇳🇱", "🇳🇨", "🇳🇿", "🇳🇮", "🇳🇪", "🇳🇬", "🇳🇪", "🇳🇮",
             "🇳🇿", "🇳🇨", "🇳🇱", "🇳🇷", "🇳🇦", "🇲🇲", "🇲🇿", "🇲🇦", "🇲🇸", "🇲🇪", "🇲🇺", "🇾🇹", "🇲🇽", "🇫🇲", "🇲🇩", "🇲🇨", "🇲🇳", "🇲🇷",
             "🇲🇶", "🇲🇭", "🇲🇹", "🇲🇱", "🇲🇻", "🇲🇾", "🇱🇾", "🇱🇮", "🇱🇹", "🇱🇺", "🇲🇴", "🇲🇬", "🇲🇼", "🇱🇷", "🇱🇸", "🇱🇧", "🇱🇻", "🇱🇦", "🇰🇬",
             "🇰🇼", "🇯🇪", "🇯🇴", "🇰🇿", "🇰🇪", "🇰🇮", "🇽🇰", "🇯🇵", "🇯🇲", "🇮🇹", "🇮🇱", "🇮🇲", "🇮🇪", "🇮🇶", "🇭🇳", "🇭🇰", "🇭🇺", "🇮🇸", "🇮🇳", "🇮🇩",
             "🇮🇷", "🇭🇹", "🇬🇾", "🇬🇼", "🇬🇳", "🇬🇬", "🇬🇹", "🇬🇺", "🇬🇵", "🇬🇩", "🇬🇱", "🇬🇷", "🇬🇮", "🇬🇭", "🇩🇪", "🇬🇪", "🇬🇲", "🇬🇦", "🇹🇫",
             "🇵🇫", "🇬🇫", "🇫🇷", "🇸🇿", "🇪🇹", "🇪🇺", "🇫🇰", "🇫🇴", "🇫🇯", "🇫🇮", "🇪🇪", "🇪🇷", "🇬🇶", "🇸🇻", "🇪🇬", "🇪🇨", "🇩🇴", "🇨🇺", "🇨🇼", "🇨🇾",
             "🇨🇿", "🇩🇰", "🇩🇯", "🇩🇲", "🇭🇷", "🇨🇮", "🇨🇷", "🇨🇰", "🇨🇩", "🇨🇬", "🇰🇲", "🇹🇩", "🇮🇴", "🇨🇱", "🇨🇳", "🇨🇽", "🇨🇨", "🇨🇴", "🇨🇫", "🇰🇾",
             "🇧🇶", "🇨🇻", "🇮🇨", "🇨🇦", "🇨🇲", "🇧🇷", "🇻🇬", "🇧🇳", "🇧🇬", "🇧🇫", "🇧🇮", "🇰🇭", "🇧🇼", "🇧🇦", "🇧🇴", "🇧🇹", "🇧🇲", "🇧🇯", "🇧🇿", "🇦🇿",
             "🇧🇸", "🇧🇭", "🇧🇩", "🇧🇧", "🇧🇾", "🇧🇪", "🇦🇹", "🇦🇺", "🇦🇼", "🇦🇲", "🇦🇷", "🇦🇬", "🇦🇶", "🇦🇮", "🇦🇴", "🇦🇩", "🇦🇸", "🇩🇿", "🇦🇱", "🇦🇽",
             "🇦🇫", "🇺🇳", "🏳️‍⚧️", "🏳️‍🌈", "🏳‍🌈"]

