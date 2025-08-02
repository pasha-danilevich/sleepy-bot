from aiogram.fsm.state import State, StatesGroup


class EditDreamSG(StatesGroup):
    edit = State()
    done = State()
