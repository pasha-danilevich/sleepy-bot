from aiogram.fsm.state import State, StatesGroup


class TrackingSG(StatesGroup):
    start = State()
    sleep = State()
    wakeup = State()
    rating = State()
