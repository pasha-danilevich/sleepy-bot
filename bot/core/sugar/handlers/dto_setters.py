"""Простые, часто используемые обработчики-сеттеры для DTO по имени атрибута.
Сеттеры надо использовать в on_click: on_click=SetterForButton.set_value(value='foo', attr_name='some_name')"""

from functools import partial
from typing import Any, Literal

from aiogram.fsm.state import State
from aiogram.types import CallbackQuery
from aiogram_dialog import Data
from aiogram_dialog.widgets.kbd.button import Button, OnClick
from aiogram_dialog.widgets.kbd.select import Multiselect, OnItemClick, Select

from bot.core.dialog_manager.custom_dialog_manager import DialogManagerWithDTO


class SetterForButton:
    """Установить определенное значение в определенный атрибут DTO диалога.
    Лучше использовать в связке с [Start, SwitchTo, Next, Back] для перемещения по диалогу
    """

    @classmethod
    def set_value(cls, value: Any, attr_name: str) -> OnClick:
        return partial(cls._on_click, value=value, attr_name=attr_name)

    @staticmethod
    async def _on_click(
        _: CallbackQuery,
        __: Button,
        manager: DialogManagerWithDTO,
        value: Data,
        attr_name: str,
    ):
        setattr(manager.dto, attr_name, value)


class SetterForSelect:
    """Простой способ установить значение по ключу в dialog_data
    Значение установится в зависимости от нажатой кнопки.
    Производит переключение между окнами или диалогами"""

    @classmethod
    def set_selected_value_and_move(
        cls, attr_name: str, event_type: Literal['start', 'switch'], state: State
    ) -> OnItemClick:
        return partial(
            cls._on_select_click,
            attr_name=attr_name,
            event_type=event_type,
            state=state,
        )

    @staticmethod
    async def _on_select_click(
        _: CallbackQuery,
        __: Select,
        manager: DialogManagerWithDTO,
        item_id: str,
        attr_name: str,
        event_type: Literal['start', 'switch'],
        state: State,
    ) -> None:
        setattr(manager.dto, attr_name, item_id)

        match event_type:
            case 'start':
                await manager.start(state=state)
            case 'switch':
                await manager.switch_to(state=state)


class DTOSetterForMultiselect:
    """Установит выбранные значения в DTO, которое использует диалог.
    Зависит от DTO, поэтому необходимо инициализировать DTO в dialog_data"""

    @classmethod
    def set_selected_value(
        cls,
        attr_name: str,
    ) -> OnItemClick:
        return partial(
            cls._on_multiselect,
            attr_name=attr_name,
        )

    @staticmethod
    async def _on_multiselect(
        _: CallbackQuery,
        __: Multiselect,
        manager: DialogManagerWithDTO,
        item_id: int,
        attr_name: str,
    ) -> None:
        """Обработка множественного выбора"""

        selected = getattr(manager.dto, attr_name)

        if item_id in selected:
            selected.remove(item_id)
        else:
            selected.append(item_id)

        setattr(manager.dto, attr_name, selected)
