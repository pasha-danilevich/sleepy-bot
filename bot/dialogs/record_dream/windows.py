from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Back, Cancel
from aiogram_dialog.widgets.text import Const

from .state import RecordDreamSG
from ...core.sugar.handlers.dialog_data_setters import TextInputWithSetter

windows = [
    Window(
        Const("Постарайтесь вспомнить и описать свой сон:"),
        TextInputWithSetter(key='dream_text', event_type='switch', state=RecordDreamSG.done),
        Cancel(Const('Назад')),
        state=RecordDreamSG.start,
    ),
    Window(
        Const('Отлично. Вы можете найти свой сон в вкладке "Мои сновидения"'),
        Back(Const('Назад, изменить текст')),
        Cancel(Const('Закрыть')),
        state=RecordDreamSG.done,
    ),
]
