from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

import keyboards.admin as admin_kb
import keyboards.user as user_kb
import states.admin as states
from config import admin_id
from handlers import texts
from create_bot import dp
from utils import db


@dp.callback_query_handler(admin_kb.order_data.filter())
async def send_video_to_user(call: CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = callback_data["user_id"]

    await states.SendVideo.enter_video.set()
    await state.update_data(user_id=user_id)
    await call.message.answer(texts.SendVideo.enter_video)
    await call.answer()


@dp.message_handler(state=states.SendVideo.enter_video, content_types="video")
async def enter_video(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.bot.send_video(user_data["user_id"], message.video.file_id, caption=texts.order_for_user)

    await message.answer(texts.SendVideo.finish)
    await state.finish()


@dp.message_handler(text="Настройки", user_id=admin_id)
async def settings(message: Message):
    await message.answer(texts.admin_settings, reply_markup=admin_kb.settings)


@dp.message_handler(Text(startswith="Изменить цену"), user_id=admin_id)
async def change_price(message: Message, state: FSMContext):
    await message.answer(texts.Settings.enter_price, reply_markup=user_kb.cancel)
    await states.Settings.enter_price.set()
    await state.update_data(currency=message.text.split()[2])


@dp.message_handler(state=states.Settings.enter_price)
async def enter_price(message: Message, state: FSMContext):
    try:
        price = int(message.text)
    except ValueError:
        await message.answer("Введите целое число")
        return
    fsm_data = await state.get_data()
    db.change_price(price, fsm_data["currency"])
    await message.answer(texts.Settings.finish)
    await state.finish()


@dp.message_handler(text="Изменить канал", user_id=admin_id)
async def change_channel(message: Message):
    await message.answer(texts.Settings.enter_channel_id, reply_markup=user_kb.cancel)

    await states.Settings.enter_channel_id.set()


@dp.message_handler(state=states.Settings.enter_channel_id)
async def enter_channel_id(message: Message, state: FSMContext):
    try:
        channel_id = int(message.text)
    except ValueError:
        await message.answer("Введите целое число")
        return
    await state.update_data(id=channel_id)
    await message.answer(texts.Settings.enter_channel_url)
    await states.Settings.next()


@dp.message_handler(state=states.Settings.enter_channel_url)
async def enter_channel_id(message: Message, state: FSMContext):
    await state.update_data(url=message.text)
    channel_data = await state.get_data()
    db.change_channel(channel_data)
    await message.answer(texts.Settings.finish)
    await state.finish()
