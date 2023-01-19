from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(KeyboardButton("Купить"))

menu_with_trial = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(KeyboardButton("Купить"),
                                                                             KeyboardButton("Пробное видео"))

cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Отмена"))

skip = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Пропустить"))


def get_channel_url(url):
    return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("Подписаться", url=url))
