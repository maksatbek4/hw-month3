from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, exstra, admin, fsmAdminMentor

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_hendler_admin(dp)
fsmAdminMentor.register_handlers_fsm_anketa(dp)

exstra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)




