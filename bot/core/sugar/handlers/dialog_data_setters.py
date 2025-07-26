"""Простые, часто используемые обработчики-сеттеры для dialog_data по ключу
Сеттеры надо использовать в on_click: on_click=SetterForButton.set_value(value='foo', key='some_name')"""

from functools import partial
from typing import Literal, Union

from aiogram.fsm.state import State
from aiogram.types import CallbackQuery
from aiogram_dialog import Data, DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.input.text import OnSuccess
from aiogram_dialog.widgets.kbd import Button, Multiselect
from aiogram_dialog.widgets.kbd.button import OnClick
from aiogram_dialog.widgets.kbd.select import OnItemClick, Select


class SetterForButton:
    """Установить значение по ключу в dialog_data.
    Лучше использовать в связке с [Start, SwitchTo, Next, Back] для перемещения по диалогу
    """

    @classmethod
    def set_value(cls, value: Data, key: str | int) -> OnClick:
        return partial(cls._on_click, value=value, key=key)

    @staticmethod
    async def _on_click(
        _: CallbackQuery,
        __: Button,
        manager: DialogManager,
        value: Data,
        key: str | int,
    ) -> None:
        manager.dialog_data[key] = value


class SetterForSelected:
    """Установить значение по ключу в dialog_data
    Значение установится в зависимости от нажатой кнопки.
    Производит переключение между окнами или диалогами"""

    @classmethod
    def set_selected_value_and_move(
        cls, key: str | int, event_type: Literal['start', 'switch'], state: State
    ) -> Union[OnItemClick, OnSuccess]:
        return partial(cls._on_select_click, key=key, event_type=event_type, state=state)

    @staticmethod
    async def _on_select_click(
        _: CallbackQuery,
        __: Select,
        manager: DialogManager,
        item_id: str,
        key: str | int,
        event_type: Literal['start', 'switch'],
        state: State,
    ) -> None:
        manager.dialog_data[key] = item_id

        match event_type:
            case 'start':
                await manager.start(state=state)
            case 'switch':
                await manager.switch_to(state=state)


class SetterForMultiselect:
    """Простой способ установить значение по ключу в dialog_data
    Значение установится в зависимости от выбранных кнопок."""

    @classmethod
    def set_to_key(
        cls,
        key: str | int,
    ) -> OnItemClick:
        return partial(
            cls._on_multiselect,
            key=key,
        )

    @staticmethod
    async def _on_multiselect(
        _: CallbackQuery,
        __: Multiselect,
        manager: DialogManager,
        item_id: int,
        key: str | int,
    ) -> None:
        """Обработка множественного выбора"""
        selected = manager.dialog_data.setdefault(key, [])

        if item_id in selected:
            selected.remove(item_id)
        else:
            selected.append(item_id)

        manager.dialog_data[key] = selected


class TextInputWithSetter(TextInput, SetterForSelected):
    def __init__(self, key: str, event_type: Literal['start', 'switch'], state: State):
        super().__init__(
            id=f'text_input_{key}',
            on_success=self.set_selected_value_and_move(  # type: ignore[arg-type]
                key=key,
                event_type=event_type,
                state=state,
            ),
        )
