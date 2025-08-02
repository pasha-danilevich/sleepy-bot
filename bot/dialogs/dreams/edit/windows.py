from aiogram.enums.parse_mode import ParseMode
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, Row
from aiogram_dialog.widgets.text import Const, Format

from . import getters, handlers
from .state import EditDreamSG

windows = [
    Window(
        Const("На данный момент, ваш сон звучит так:"),
        Const(" "),
        Format('`{dream_text}`'),
        Const(" "),
        Const("Скопируйте его, измените и отправьте."),
        TextInput(id='text', on_success=handlers.on_input_dream_text),
        Cancel(Const("Назад")),
        state=EditDreamSG.edit,
        getter=[getters.get_dream_text],
        parse_mode=ParseMode.MARKDOWN,
    ),
    Window(
        Const('Отлично. Вы можете найти свой сон в вкладке "Мои сновидения"'),
        Row(
            Cancel(Const("Закрыть")),
        ),
        state=EditDreamSG.done,
    ),
]
