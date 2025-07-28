from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Back, Button, Cancel, Group, Row, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from . import getters, handlers
from .state import TrackingSG

main_window = Window(
    Const("Выберите действие:"),
    Row(
        SwitchTo(
            Const("Проснулся"),
            id="wake_up",
            state=TrackingSG.wakeup,
            when='is_sleeping',
            on_click=handlers.on_wakeup,
        ),
        SwitchTo(
            Const("Иду спать"),
            id="go_to_sleep",
            state=TrackingSG.sleep,
            when='is_awake',
            on_click=handlers.go_to_sleep,
        ),
    ),
    Cancel(Const("Назад")),
    getter=getters.get_sleep_state,
    state=TrackingSG.start,
)

sleep_window = Window(
    Const("Хорошо, записал. Спокойной ночи"),
    Cancel(Const("На главную")),
    state=TrackingSG.sleep,
)

wakeup_window = Window(
    Format("Доброе утро.\nВы спали: {sleep_duration}"),
    Group(
        Row(
            Button(
                Const("Записать сновидение"), id='record', on_click=handlers.start_record_dream
            ),
            SwitchTo(Const("Оценить качество сна"), id="rate_sleep", state=TrackingSG.rating),
        ),
        Cancel(Const("На главную")),
    ),
    state=TrackingSG.wakeup,
    getter=getters.get_sleep_duration,
)

rating_window = Window(
    Const("Выберите оценку:"),
    Group(
        Button(Const("⭐️"), id="rating_1"),
        Button(Const("⭐️⭐️"), id="rating_2"),
        Button(Const("⭐️⭐️⭐️"), id="rating_3"),
        Button(Const("⭐️⭐️⭐️⭐️"), id="rating_4"),
        Button(Const("⭐️⭐️⭐️⭐️⭐️"), id="rating_5"),
        Row(
            Back(Const("Назад")),
            Cancel(Const("На главную")),
        ),
    ),
    state=TrackingSG.rating,
)

windows = [main_window, sleep_window, wakeup_window, rating_window]
