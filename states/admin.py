from aiogram.dispatcher.filters.state import StatesGroup, State


class SendVideo(StatesGroup):
    enter_video = State()


class Settings(StatesGroup):
    enter_price = State()
    enter_channel_id = State()
    enter_channel_url = State()
