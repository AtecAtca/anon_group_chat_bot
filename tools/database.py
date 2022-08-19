import psycopg2 as pg
from string import ascii_uppercase
from random import choice
from tools.logger import get_logger
from tools.messages import all_symbols
import os

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
# GET
#=======================================================================================================================
    async def get(self,
                  items: tuple,
                  table_name: str,
                  condition: dict,
                  order_by: dict=None,
                  fetchall=False,):

        key, value = tuple(condition.items())[0]
        query = f'SELECT {", ".join(items)} FROM {table_name} WHERE {key} = %s'

        with self.conn:
            with self.conn.cursor() as cur:
                if order_by is not None:
                    query += ' ORDER BY {} {}'.format(*tuple(order_by.items())[0])

                cur.execute(query, (value,))
                result = cur.fetchall() if fetchall else cur.fetchone()
                if result is None:
                    logger.debug(f'method db.get: return result=None')
                    return None
                else:
                    if len(items) == 1:
                        logger.debug(f'method db.get: return result={result[0]}')
                        return result[0]
                    else:
                        logger.debug(f'method db.get: return result={result}')
                        return result
# UPDATE
#=======================================================================================================================
    async def update(self,
                     items: dict,
                     table_name: str,
                     condition: dict,
                     array_func: str=None):

        item_key, item_value = tuple(items.items())[0]
        condition_key, condition_value = tuple(condition.items())[0]

        if array_func is None:
            query = f'UPDATE {table_name} SET {item_key} = %s WHERE {condition_key} = %s;'
        else:
            query = f'UPDATE {table_name} SET {item_key} = {array_func}({item_key}, %s) WHERE {condition_key} = %s;'

        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.update: {query}, {item_value, condition_value}')
                cur.execute(query, (item_value, condition_value))

    async def update_many(self,
                          items: dict,
                          table_name: str,
                          condition: dict,
                          set_pool='SET ',
                          item_values=None):

        if item_values is None:
            item_values = []
        condition_key, condition_value = tuple(condition.items())[0]

        for key, value in items.items():
            item_values.append(value)
            set_pool += f'{key} = %s, '
        query = f'UPDATE {table_name} {set_pool[:-2]} WHERE {condition_key} = %s;'

        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.update_many: {query}, {*item_values, condition_value}')
                cur.execute(query, (*item_values, condition_value))

# INSERT
#=======================================================================================================================
    async def insert(self, items: dict, table_name: str):
        keys = [key for key in items.keys()]
        values = [value for value in items.values()]
        columns = (", ".join(keys)).replace("'", '')
        columns_values = "%s, " * len(keys)
        query = f'INSERT INTO {table_name} ({columns}) VALUES ({columns_values[:-2]});'
        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.insert: {query}, {values}')
                cur.execute(query, values)

# CODE
#=======================================================================================================================
    def create_code(self) -> str:
        code = ''
        for i in range(1, 5):
            code += str(choice(ascii_uppercase))
        logger.debug(f'method db.create_code: return code={code}')
        return code

    async def get_unique_code(self) -> str:
        code = self.create_code()
        while await self.get(table_name='users',
                             items=('code',),
                             condition={'code': code}) is not None:
            code = self.create_code()
        logger.debug(f'method db.get_unique_code: return code={code}')
        return code

    def is_nickname_in_all_symbols(self, nickname: str) -> bool:
        for i in nickname.lower():
            if i not in all_symbols:
                logger.debug(f'method db.is_nickname_in_all_symbols: return False')
                return False
        logger.debug(f'method db.is_nickname_in_all_symbols: return True')
        return True



    async def get_chat_members(self, uid: int, with_language=False):
        if with_language:
            query = "SELECT * FROM get_chat_members_with_language(%s);"
        else:
            query = "SELECT * FROM get_chat_members_with_not_language(%s);"

        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.get_chat_members: {query}')
                cur.execute(query, (uid,))
                result = cur.fetchall()
                if result is None:
                    logger.debug(f'method db.get_chat_members: return result=None')
                    return None
                else:
                    logger.debug(f'method db.get_chat_members: return result={result}')
                    return result




    async def get_chat_name(self, uid):
        query = "SELECT chat_name FROM chats WHERE chat_code = get_chat_code(%s);"
        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.get_chat_name: {query}')
                cur.execute(query, (uid,))
                result = cur.fetchone()
                if result is None:
                    logger.debug(f'method db.get_chat_name: return result=None')
                    return None
                else:
                    logger.debug(f'method db.get_chat_name: return result={result[0]}')
                    return result[0]


    async def get_public_chats_data(self):
        query = """SELECT chats.chat_name, 
                          chats.chat_code,
	                      COUNT(users.in_chat) AS count_
                   FROM chats
                   LEFT JOIN users
                   ON chats.chat_code = users.in_chat
                   GROUP BY chats.chat_code, chats.chat_name
                   ORDER BY count_ DESC"""
        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.get_public_chats_data: {query}')
                cur.execute(query)
                result = cur.fetchall()
                logger.debug(f'method db.get_public_chats_data: return result={result}')
                return result

    async def get_non_active_members_data(self):
        query = """ SELECT tg_id, language FROM users
                    WHERE in_chat IS NOT NULL
                    AND last_activity-interval'3 hours' 
                    NOT BETWEEN clock_timestamp()-interval'24 hours' AND clock_timestamp()
                    ORDER BY last_activity DESC;;"""
        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.get_non_active_members_data: {query}')
                cur.execute(query)
                result = cur.fetchall()
                if result is not None:
                    logger.debug(f'method db.get_non_active_members_data: return result={result}')
                    return result
            logger.debug(f'method db.get_non_active_members_data: return result=None')


    async def get_list_of_chat_members(self, uid):
        query = """ SELECT tg_id, nickname, flag,
                    clock_timestamp() - (last_activity - interval'3 hours')
                    FROM users WHERE in_chat = get_chat_code(%s)
                    ORDER BY last_activity DESC;"""
        with self.conn:
            with self.conn.cursor() as cur:
                logger.debug(f'method db.get_list_of_chat_members: {query}')
                cur.execute(query, (uid,))
                result = cur.fetchall()
                if result is not None:
                    logger.debug(f'method db.get_list_of_chat_members: return result={result}')
                    return result
            logger.debug(f'method db.get_list_of_chat_members: return result=None')



logger = get_logger('main.tools.database')
db = dataBase('web')
#db = dataBase('local')




