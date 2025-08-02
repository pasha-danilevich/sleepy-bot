from aiogram.fsm.state import State, StatesGroup


class RetrieveDreamSG(StatesGroup):
    dream = State()
    no_dream = State()
