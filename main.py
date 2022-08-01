from aiogram.utils import executor
from tools.logger import get_logger
from tools.bot import bot, dp
from tools.database import db
from handlers.commands import commands_handlers
from handlers.messages import message_handlers
from handlers.callbacks import callback_handlers
import os

async def on_startup(_):
    bot.set_webhook(os.environ.get('URL_APP'))
    logger.info('Executor started.')

async def on_shutdown(_):
    bot.delete_webhook()
    db.close_on_shutdown()
    logger.info('Executor finished.')

def start(type):
    if type == 'local':
        executor.start_polling(dp, skip_updates=True)
    else:
        executor.start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)))


logger = get_logger('main.py')

commands_handlers(dp)
callback_handlers(dp)
message_handlers(dp)

if __name__ == '__main__':
    #start('local')
    start('web')




