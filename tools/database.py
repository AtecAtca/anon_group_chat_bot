from aiogram import types
import psycopg2 as pg
from psycopg2.errors import UniqueViolation
from string import ascii_uppercase
from random import choice
import os
from tools.logger import get_logger

class dataBase():
    def __init__(self, type):
        self.DATABASE_URL = os.getenv('DATABASE_URL') if type == 'local' else os.environ.get('DATABASE_URL')
        try:
            self.conn = pg.connect(self.DATABASE_URL, sslmode='require')
        except Exception as e:
            logger.debug(f'DATABASE_URL = {self.DATABASE_URL}')
            logger.exception(e)
        else:
            self.cur = self.conn.cursor()
            logger.info('Database connected successfully')

    def close_on_shutdown(self):
        self.cur.close()
        self.conn.close()


logger = get_logger('main.tools.database')
db = dataBase('web')
#db = dataBase('local')