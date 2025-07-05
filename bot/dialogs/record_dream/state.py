from aiogram.fsm.state import State, StatesGroup


class RecordDreamSG(StatesGroup):
    start = State()
    done = State()
