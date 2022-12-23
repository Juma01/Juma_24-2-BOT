from aiogram.utils import executor
import logging
from config import dp
from handlers import client, callback, extra, admin, fsm_anketa, fsmAdminMentor
from database.bot_db import sql_create


client.register_handlers_client(dp)
callback.register_handler_callback(dp)
admin.register_handler_admin(dp)
# fsm_anketa.register_handlers_fsm_anketa(dp)
fsmAdminMentor.register_handlers_fsmAdminMentor(dp)

extra.register_handlers_extra(dp)


async def on_startup(_):
    sql_create()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)