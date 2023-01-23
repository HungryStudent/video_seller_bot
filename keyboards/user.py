from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

select_lang = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton("Русский 🇷🇺", callback_data="lang:ru"),
                                                    InlineKeyboardButton("Английский 🇺🇸", callback_data="lang:en"))

buy = {"ru": "Купить", "en": "Buy"}
support = {"ru": "Поддержка", "en": "Support"}
trial_video = {"ru": "Пробное видео в низком качестве", "en": "Trial video in low quality"}
cancel = {"ru": "Отмена", "en": "Cancel"}
skip = {"ru": "Пропустить", "en": "Skip"}
subscribe = {"ru": "Подписаться", "en": "Subscribe"}
pay = {"ru": "Оплатить", "en": "To pay"}
start_over = {"ru": "Начать сначала", "en": "Start over"}
feedback = {"ru": "Оставить отзыв", "en": "Leave feedback"}
feedback_channel = {"ru": "Отзывы", "en": "Feedbacks"}


def get_menu(lang):
    return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(KeyboardButton(buy[lang]),
                                                                      KeyboardButton(feedback_channel[lang]))


def get_start_over(lang):
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(start_over[lang]))


def get_menu_with_trial(lang):
    return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(KeyboardButton(buy[lang]),
                                                                      KeyboardButton(trial_video[lang]),
                                                                      KeyboardButton(feedback_channel[lang]))


def get_cancel(lang):
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(cancel[lang]))


def get_skip(lang):
    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton(skip[lang]))


def get_channel_url(url, lang):
    return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(subscribe[lang], url=url),
                                                 InlineKeyboardButton(start_over[lang], callback_data="start_over"))


def get_pay(pay_url, lang):
    return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(pay[lang], url=pay_url),
                                                 InlineKeyboardButton(start_over[lang], callback_data="start_over"))


def get_order(order_id, lang):
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(feedback[lang], callback_data=f"feedback:{order_id}"),
        InlineKeyboardButton(start_over[lang], callback_data="start_over"))
