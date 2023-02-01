from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

import keyboards.admin as admin_kb
import keyboards.user as user_kb
import states.user as states
from config import admin_id, feedback_chat_id
from handlers import texts
from create_bot import dp
from utils import db, pay


@dp.message_handler(commands='start')
@dp.message_handler(text="В главное меню")
@dp.message_handler(text="Начать сначала")
@dp.message_handler(text="Start over")
async def start_message(message: Message):
    lang = db.get_lang(message.from_user.id)
    user = db.get_user(message.from_user.id)
    if user is None:
        await message.answer(texts.choose_lang, reply_markup=user_kb.select_lang)
    elif message.from_user.id == admin_id:
        await message.answer(texts.hello_admin, reply_markup=admin_kb.menu)
    elif user["trial"]:
        await message.answer(texts.hello[lang], reply_markup=user_kb.get_menu_with_trial(lang))
    else:
        await message.answer(texts.hello[lang], reply_markup=user_kb.get_menu(lang))


@dp.callback_query_handler(Text(startswith="lang"))
async def reg_user(call: CallbackQuery):
    lang = db.get_lang(call.from_user.id)
    user = db.get_user(call.from_user.id)
    if user:
        await call.message.delete()
        return

    if call.from_user.id == admin_id:
        await call.message.answer(texts.hello_admin, reply_markup=admin_kb.menu)
    else:
        await call.message.answer(texts.hello[lang], reply_markup=user_kb.get_menu_with_trial(lang))
    db.add_user(call.from_user.id, call.from_user.username, call.from_user.first_name, call.data.split(":")[1])
    await call.message.delete()


@dp.callback_query_handler(text="gift_video")
async def gift_video(call: CallbackQuery):
    lang = db.get_lang(call.from_user.id)
    await call.message.answer(texts.Video.enter_url[lang], reply_markup=user_kb.get_cancel(lang))
    await states.CreateVideo.enter_url.set()


@dp.callback_query_handler(text="start_over")
async def start_over(call: CallbackQuery):
    lang = db.get_lang(call.from_user.id)
    user = db.get_user(call.from_user.id)
    if user is None:
        await call.message.answer(texts.choose_lang, reply_markup=user_kb.select_lang)
    elif call.from_user.id == admin_id:
        await call.message.answer(texts.hello_admin, reply_markup=admin_kb.menu)
    elif user["trial"]:
        await call.message.answer(texts.hello[lang], reply_markup=user_kb.get_menu_with_trial(lang))
    else:
        await call.message.answer(texts.hello[lang], reply_markup=user_kb.get_menu(lang))
    await call.answer()


@dp.message_handler(state="*", text="Отмена")
@dp.message_handler(state="*", text="Cancel")
async def cancel_input(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.finish()
    user = db.get_user(message.from_user.id)
    if message.from_user.id == admin_id:
        await message.answer(texts.hello_admin, reply_markup=admin_kb.menu)
    elif user["trial"]:
        await message.answer(texts.hello[lang], reply_markup=user_kb.get_menu_with_trial(lang))
    else:
        await message.answer(texts.hello[lang], reply_markup=user_kb.get_menu(lang))


@dp.message_handler(text="Отзывы")
@dp.message_handler(text="Feedbacks")
async def feedbacks(message: Message):
    lang = db.get_lang(message.from_user.id)
    await message.answer(texts.feedbacks[lang])


@dp.message_handler(text="Купить")
@dp.message_handler(text="Buy")
async def start_buy(message: Message):
    lang = db.get_lang(message.from_user.id)
    await message.answer(texts.Video.enter_url[lang], reply_markup=user_kb.get_cancel(lang))
    await states.CreateVideo.enter_url.set()


@dp.message_handler(text="Пробное видео в низком качестве")
@dp.message_handler(text="Trial video in low quality")
async def trial(message: Message):
    lang = db.get_lang(message.from_user.id)
    user = db.get_user(message.from_user.id)
    if user["trial"]:
        await message.answer(texts.TrialVideo.enter_url[lang], reply_markup=user_kb.get_cancel(lang))
        await states.CreateTrialVideo.enter_url.set()
    else:
        await message.answer(texts.trial_error[lang])


@dp.message_handler(state=states.CreateTrialVideo.enter_url)
async def enter_url(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.update_data(url=message.text)

    await message.answer(texts.TrialVideo.enter_logo[lang])
    await states.CreateTrialVideo.next()


@dp.message_handler(state=states.CreateTrialVideo.enter_logo, content_types="photo")
async def enter_logo(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.update_data(logo=message.photo[-1].file_id)

    await message.answer(texts.TrialVideo.enter_text[lang], reply_markup=user_kb.get_skip(lang))
    await states.CreateTrialVideo.next()


@dp.message_handler(state=states.CreateTrialVideo.enter_logo, content_types="document")
async def error_logo_trial(message: Message, state: FSMContext):
    await message.answer("Пришлите логотип как фото, а не как документ")


@dp.message_handler(state=states.CreateTrialVideo.enter_text)
async def enter_logo_trial(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    text = message.text
    if message.text in ["Пропустить", "Skip"]:
        text = "-"
    await state.update_data(text=text)

    video_data = await state.get_data()
    await message.bot.send_photo(admin_id, video_data["logo"],
                                 caption=texts.new_trial_order[lang].format(username=message.from_user.username,
                                                                            url=video_data["url"],
                                                                            text=video_data["text"]),
                                 reply_markup=admin_kb.new_order(message.from_user.id, 0))
    await message.answer(texts.TrialVideo.finish[lang], reply_markup=user_kb.get_start_over(lang))
    db.change_trial(message.from_user.id)
    await state.finish()


@dp.message_handler(state=states.CreateVideo.enter_url)
async def enter_url(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.update_data(url=message.text)

    await message.answer(texts.Video.enter_logo[lang])
    await states.CreateVideo.next()


@dp.message_handler(state=states.CreateVideo.enter_logo, content_types="photo")
async def enter_logo(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await state.update_data(logo=message.photo[-1].file_id)

    await message.answer(texts.Video.enter_text[lang], reply_markup=user_kb.get_skip(lang))
    await states.CreateVideo.next()


@dp.message_handler(state=states.CreateVideo.enter_logo, content_types="document")
async def error_logo(message: Message, state: FSMContext):
    await message.answer("Пришлите логотип как фото, а не как документ")


@dp.message_handler(state=states.CreateVideo.enter_text)
async def enter_logo(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    text = message.text
    if message.text in ["Пропустить", "Skip"]:
        text = "-"
    await state.update_data(text=text)

    video_data = await state.get_data()
    user = db.get_user(message.from_user.id)
    if user["feedback_gift"]:
        await message.bot.send_photo(admin_id, video_data["logo"],
                                     caption=texts.new_gift_order[lang].format(username=message.from_user.username,
                                                                               url=video_data["url"],
                                                                               text=video_data["text"]),
                                     reply_markup=admin_kb.new_order(message.from_user.id, 0))
        db.remove_feedback_gift(message.from_user.id)
        await message.answer(texts.Video.gift[lang], reply_markup=user_kb.get_menu(lang))
    else:
        price = db.get_price(lang)["price"]
        order_id = db.create_order(message.from_user.id, video_data)
        pay_urls = pay.get_urls(order_id, price, lang)
        await message.answer(texts.Video.pay[lang].format(price=price),
                             reply_markup=user_kb.get_pay(pay_urls, lang))
    await state.finish()


@dp.callback_query_handler(Text(startswith="feedback"))
async def stay_feedback(call: CallbackQuery, state: FSMContext):
    lang = db.get_lang(call.from_user.id)
    order_id = int(call.data.split(":")[1])
    if db.get_order(order_id)["have_feedback"]:
        await call.answer("Вы уже оставили отзыв по этому заказу")
        return
    await states.StayFeedback.enter_feedback.set()
    await state.update_data(order_id=order_id)
    await call.message.answer(texts.StayFeedback.enter_feedback[lang])
    await call.answer()


@dp.message_handler(state=states.StayFeedback.enter_feedback)
async def enter_feedback(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    data = await state.get_data()
    db.change_feedback_status(data["order_id"], message.from_user.id)
    await message.answer(texts.StayFeedback.finish[lang], reply_markup=user_kb.get_gift(lang))
    await message.forward(feedback_chat_id)
    await state.finish()
