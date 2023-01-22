from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(KeyboardButton("Купить"),
                                                                  KeyboardButton("Поддержка"))

start_over = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Начать сначала"))

menu_with_trial = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(KeyboardButton("Купить"),
                                                                             KeyboardButton(
                                                                                 "Пробное видео в низком качестве"),
                                                                             KeyboardButton("Поддержка"))

cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Отмена"))

skip = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton("Пропустить"))


def get_channel_url(url):
    return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Подписаться", url=url))


def get_pay(pay_url):
    return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Оплатить", url=pay_url))
