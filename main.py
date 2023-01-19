from middlewares.subscribe import CheckSubMiddleware
from aiogram.utils import executor

from handlers import users
from handlers import admin
from create_bot import dp
from utils import db


dp.middleware.setup(CheckSubMiddleware())


async def on_startup(_):
    db.start()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
