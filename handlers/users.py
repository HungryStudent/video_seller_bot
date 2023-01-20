from aiogram.dispatcher import FSMContext
from aiogram.types import Message

import keyboards.admin as admin_kb
import keyboards.user as user_kb
import states.user as states
from config import admin_id
from handlers import texts
from create_bot import dp
from utils import db


@dp.message_handler(commands='start')
@dp.message_handler(text="В главное меню")
async def start_message(message: Message):
    user = db.get_user(message.from_user.id)
    if user is None:
        if message.from_user.id == admin_id:
            await message.answer(texts.hello_admin, reply_markup=admin_kb.menu)
        else:
            await message.answer(texts.hello, reply_markup=user_kb.menu_with_trial)
        db.add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, "ru")
    elif message.from_user.id == admin_id:
        await message.answer(texts.hello_admin, reply_markup=admin_kb.menu)
    elif user["trial"]:
        await message.answer(texts.hello, reply_markup=user_kb.menu_with_trial)
    else:
        await message.answer(texts.hello, reply_markup=user_kb.menu)


@dp.message_handler(state="*", text="Отмена")
async def cancel_input(message: Message, state: FSMContext):
    await state.finish()
    user = db.get_user(message.from_user.id)
    if message.from_user.id == admin_id:
        await message.answer(texts.hello_admin, reply_markup=admin_kb.menu)
    elif user["trial"]:
        await message.answer(texts.hello, reply_markup=user_kb.menu_with_trial)
    else:
        await message.answer(texts.hello, reply_markup=user_kb.menu)


@dp.message_handler(text="Купить")
async def triaasl(message: Message):
    await message.answer("В разработке (будет аналогично пробному видео, но с оплатой")


@dp.message_handler(text="Пробное видео")
async def trial(message: Message):
    user = db.get_user(message.from_user.id)
    if user["trial"]:
        await message.answer(texts.TrialVideo.enter_url, reply_markup=user_kb.cancel)
        await states.CreateTrialVideo.enter_url.set()
    else:
        await message.answer(texts.trial_error)


@dp.message_handler(state=states.CreateTrialVideo.enter_url)
async def enter_url(message: Message, state: FSMContext):
    await state.update_data(url=message.text)

    await message.answer(texts.TrialVideo.enter_logo)
    await states.CreateTrialVideo.next()


@dp.message_handler(state=states.CreateTrialVideo.enter_logo, content_types="photo")
async def enter_logo(message: Message, state: FSMContext):
    await state.update_data(logo=message.photo[-1].file_id)

    await message.answer(texts.TrialVideo.enter_text)
    await states.CreateTrialVideo.next()


@dp.message_handler(state=states.CreateTrialVideo.enter_text)
async def enter_logo(message: Message, state: FSMContext):
    text = message.text
    if message.text == "Пропустить":
        text = "-"
    await state.update_data(text=text)

    video_data = await state.get_data()
    await message.bot.send_photo(admin_id, video_data["logo"],
                                 caption=texts.new_trial_order.format(username=message.from_user.username,
                                                                      url=video_data["url"],
                                                                      text=video_data["text"]),
                                 reply_markup=admin_kb.new_order(message.from_user.id))

    await message.answer(texts.TrialVideo.finish)
    db.change_trial(message.from_user.id)
    await state.finish()
