from aiogram_dialog.widgets.kbd import Back, Cancel, Row
from aiogram_dialog.widgets.text import Const

BACK_AND_CANCEL = Row(
    Back(Const('Назад')),
    Cancel(Const("На главную")),
)
