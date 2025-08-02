from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Back, Cancel
from aiogram_dialog.widgets.text import Const

from bot.core.sugar.handlers.dialog_data_setters import TextInputWithSetter

from . import handlers
from .state import CreateDreamSG

windows = [
    Window(
        Const("Постарайтесь вспомнить и описать свой сон:"),
        TextInputWithSetter(key='dream_text', event_type='switch', state=CreateDreamSG.done),
        TextInput(id='text', on_success=handlers.input_dream_text),
        Cancel(Const('Назад')),
        state=CreateDreamSG.start,
    ),
    Window(
        Const('Отлично. Вы можете найти свой сон в вкладке "Мои сновидения"'),
        Back(Const('Назад, изменить текст')),
        Cancel(Const('Закрыть')),
        state=CreateDreamSG.done,
    ),
]
