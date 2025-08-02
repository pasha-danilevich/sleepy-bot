from aiogram.fsm.state import State, StatesGroup


class CreateDreamSG(StatesGroup):
    start = State()
    done = State()
