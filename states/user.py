from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateTrialVideo(StatesGroup):
    enter_url = State()
    enter_logo = State()
    enter_text = State()


class CreateVideo(StatesGroup):
    enter_url = State()
    enter_logo = State()
    enter_text = State()


class Record(StatesGroup):
    send_location = State()
    enter_note = State()
