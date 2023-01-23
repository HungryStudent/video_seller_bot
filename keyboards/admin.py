from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

order_data = CallbackData("order", "user_id", "order_id")

menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(KeyboardButton("Купить"),
                                                                  KeyboardButton("Пробное видео в низком качестве"),
                                                                  KeyboardButton("Отзывы"),
                                                                  KeyboardButton("Настройки"))

settings = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(KeyboardButton("Изменить цену RUB"),
                                                                      KeyboardButton("Изменить цену USD"),
                                                                      KeyboardButton("Изменить канал"),
                                                                      KeyboardButton("В главное меню"))


def new_order(user_id, order_id):
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton("📹 Отправить видео", callback_data=order_data.new(user_id, order_id)))
