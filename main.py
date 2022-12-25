from aiogram.utils import executor
import logging
from config import dp
from handlers import client, callback, extra, admin, fsm_anketa, fsmAdminMentor, notification
from database.bot_db import sql_create
import asyncio


client.register_handlers_client(dp)
callback.register_handler_callback(dp)
admin.register_handler_admin(dp)
# fsm_anketa.register_handlers_fsm_anketa(dp)
fsmAdminMentor.register_handlers_fsmAdminMentor(dp)
notification.register_handlers_notification(dp)

extra.register_handlers_extra(dp)


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)