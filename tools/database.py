from aiogram import types
import psycopg2 as pg
from psycopg2.errors import UniqueViolation
from string import ascii_uppercase
from random import choice
import os
from tools.logger import get_logger
from tools.messages import all_symbols

class dataBase():
    def __init__(self, type: str):
        self.DATABASE_URL = os.getenv('DATABASE_URL') if type == 'local' else os.environ.get('DATABASE_URL')
        try:
            self.conn = pg.connect(self.DATABASE_URL, sslmode='require')
        except Exception as e:
            logger.debug(f'DATABASE_URL = {self.DATABASE_URL}')
            logger.exception(e)
        else:
            logger.info('Database connected successfully')

    def close_on_shutdown(self) -> None:
        self.conn.close()

# REGISTER NEW USER
#=======================================================================================================================

    async def register_new_user(self, uid: int, message: types.Message, language: str) -> None:
        first_name = message.from_user.first_name
        nickname = f'user-{uid}'
        status = in_chat = None
        code = await self.get_unique_code()
        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'''"INSERT INTO users (tg_id, tg_name, nickname, language, status, in_chat, code) 
                                  VALUES ({uid}, {first_name}, {nickname}, {language}, {status}, {in_chat}, {code})"''')
                cur.execute('''INSERT INTO users (tg_id, tg_name, nickname, language, status, in_chat, code)
                               VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                              (uid, first_name, nickname, language, status, in_chat, code,))

# CODE
#=======================================================================================================================

    def create_code(self) -> str:
        code = ''
        for i in range(1, 5):
            code += str(choice(ascii_uppercase))
        logger.debug(f'method db.create_code: return code={code}')
        return code

    async def get_all_codes(self, code: str) -> list:
        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.get_all_codes: SELECT code FROM users WHERE code = {code}')
                cur.execute('SELECT code FROM users WHERE code = %s', (code,))
                result = cur.fetchall()
                logger.debug(f'method db.get_all_codes: return result={result}')
                return result

    async def get_unique_code(self) -> str:
        code = self.create_code()
        all_codes = await self.get_all_codes(code)
        while code in all_codes:
            all_codes = await self.get_all_codes()
            code = self.create_code()
        logger.debug(f'method db.get_unique_code: return code={code}')
        return code

# NICKNAME
#=======================================================================================================================

    def is_nickname_in_all_symbols(self, nickname: str) -> bool:
        for i in nickname.lower():
            if i not in all_symbols:
                logger.debug(f'method db.is_nickname_in_all_symbols: return False')
                return False
        logger.debug(f'method db.is_nickname_in_all_symbols: return True')
        return True

    async def is_nickname_unique(self, nickname: types.Message) -> bool:
        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.is_nickname_unique: SELECT nickname FROM users WHERE nickname = {nickname}')
                cur.execute('SELECT nickname FROM users WHERE nickname = %s', (nickname,))
                result = cur.fetchone()
                if result is None:
                    logger.debug(f'method db.is_nickname_unique: return True')
                    return True
                else:
                    logger.debug(f'method db.is_nickname_unique: return False')
                    return False

    async def update_nickname(self, uid: types.Message, nickname: types.Message) -> None:
        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.update_nickname: UPDATE users SET nickname = {nickname} WHERE tg_id = {uid}')
                cur.execute('UPDATE users SET nickname = %s WHERE tg_id = %s', (nickname, uid))

# STATUS
#=======================================================================================================================

    async def get_status(self, uid: types.Message) -> None or bool:
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('SELECT status FROM users WHERE tg_id= %s', (uid,))
                result = cur.fetchone()
                if result is None:
                    logger.debug(f'method db.get_user_status: return result=None')
                    return None
                else:
                    logger.debug(f'method db.get_user_status: return result={result[0]}')
                    return result[0]

    async def update_status(self, uid: types.Message, status: types.Message) -> None:
        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.update_status: UPDATE users SET status = {status} WHERE tg_id = {uid}')
                cur.execute('UPDATE users SET status = %s WHERE tg_id = %s', (status, uid))

# LANGUAGE
#=======================================================================================================================

    async def get_language(self, uid) -> str:
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('SELECT language FROM users WHERE tg_id = %s', (uid,))
                result = cur.fetchone()
                if result is None:
                    logger.debug(f'method db.get_user_language: return result=RU')
                    return 'RU'
                else:
                    logger.debug(f'method db.get_user_language: return result={result[0]}')
                    return result[0]

logger = get_logger('main.tools.database')
db = dataBase('web')
#db = dataBase('local')