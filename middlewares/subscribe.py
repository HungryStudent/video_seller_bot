from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update, ChatMember
from aiogram.utils.exceptions import ChatNotFound

from handlers.texts import sub_error
from config import admin_id
from create_bot import bot
from keyboards import user
from utils import db


class CheckSubMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update: Update, data: dict):

        if update.message:
            user_id = update.message.from_user.id
        else:
            user_id = update.callback_query.from_user.id
        channel_data = db.get_channel_config()
        try:
            status: ChatMember = await bot.get_chat_member(channel_data["id"], user_id)
            if status.status == "left":
                await bot.send_message(user_id, sub_error, reply_markup=user.get_channel_url(channel_data["url"], "ru"))
                raise CancelHandler()
        except ChatNotFound as e:
            print(e)
            await bot.send_message(admin_id, "Проблема с каналом")

