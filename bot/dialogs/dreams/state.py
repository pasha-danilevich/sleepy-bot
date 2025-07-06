from aiogram.fsm.state import State, StatesGroup


class DreamsSG(StatesGroup):
    start = State()
    new_dream = State()
    dream = State()
    edit = State()
    done = State()
