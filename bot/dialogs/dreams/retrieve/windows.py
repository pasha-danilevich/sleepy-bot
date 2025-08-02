from aiogram.enums.parse_mode import ParseMode
from aiogram_dialog import StartMode, Window
from aiogram_dialog.widgets.kbd import Button, Cancel, Row, Start
from aiogram_dialog.widgets.text import Const, Format

from ...home.state import HomeSG
from . import getters, handlers
from .state import RetrieveDreamSG

windows = [
    Window(
        Format("{selected_date}"),
        Format("Качество сна: {dream_rating}"),
        Const(" "),
        Format('`{dream_text}`'),
        Button(Const("Изменить"), id='edit', on_click=handlers.start_edit_dialog),
        Row(
            Cancel(Const('Назад')),
            Start(
                Const("На главную"), id='home', mode=StartMode.RESET_STACK, state=HomeSG.start
            ),
        ),
        state=RetrieveDreamSG.dream,
        getter=[getters.get_selected_date, getters.get_dream_text, getters.get_dream_rating],
        parse_mode=ParseMode.MARKDOWN,
    ),
    Window(
        Format("{selected_date}"),
        Const(" "),
        Const("На этот день вы не записывали сон. "),
        Button(
            Const('Записать сновидение'),
            id='create_dream',
            on_click=handlers.start_create_dream,
        ),
        Cancel(Const("Назад")),
        state=RetrieveDreamSG.no_dream,
        getter=getters.get_selected_date,
    ),
]
