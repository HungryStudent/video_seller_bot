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
@dp.message_handler(text="Начать сначала")
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


@dp.message_handler(text="Поддержка")
async def support(message: Message):
    await message.answer(texts.support)


@dp.message_handler(text="Купить")
async def start_buy(message: Message):
    await message.answer(texts.Video.enter_url, reply_markup=user_kb.cancel)
    await states.CreateVideo.enter_url.set()


@dp.message_handler(text="Пробное видео в низком качестве")
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

    await message.answer(texts.TrialVideo.enter_text, reply_markup=user_kb.skip)
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

    await message.answer(texts.TrialVideo.finish, reply_markup=user_kb.start_over)
    db.change_trial(message.from_user.id)
    await state.finish()


@dp.message_handler(state=states.CreateVideo.enter_url)
async def enter_url(message: Message, state: FSMContext):
    await state.update_data(url=message.text)

    await message.answer(texts.Video.enter_logo)
    await states.CreateVideo.next()


@dp.message_handler(state=states.CreateVideo.enter_logo, content_types="photo")
async def enter_logo(message: Message, state: FSMContext):
    await state.update_data(logo=message.photo[-1].file_id)

    await message.answer(texts.Video.enter_text, reply_markup=user_kb.skip)
    await states.CreateVideo.next()


@dp.message_handler(state=states.CreateVideo.enter_text)
async def enter_logo(message: Message, state: FSMContext):
    text = message.text
    if message.text == "Пропустить":
        text = "-"
    await state.update_data(text=text)

    video_data = await state.get_data()
    # await message.bot.send_photo(admin_id, video_data["logo"],
    #                              caption=texts.new_order.format(username=message.from_user.username,
    #                                                                   url=video_data["url"],
    #                                                                   text=video_data["text"]),
    #                              reply_markup=admin_kb.new_order(message.from_user.id))

    price = db.get_price()["price"]
    await message.answer(texts.Video.pay.format(price=price), reply_markup=user_kb.get_pay("https://freekassa.ru/"))
    await state.finish()
