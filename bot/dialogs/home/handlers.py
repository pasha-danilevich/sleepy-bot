from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject
from domain.services.user_service import UserService
from tg_bot.dialogs.user_dialogs.registration.state import RegistrationSG


@inject
async def on_start(
    _,
    manager: DialogManager,
    service: FromDishka[UserService],
) -> None:
    is_complete_pregnancy = await service.is_complete_pregnancy_survey(
        manager.event.from_user.id
    )
    if is_complete_pregnancy:
        pass  # пропускаем на домашний диалог
    else:  # анкета не заполнена: запускаем диалог, чтобы ввести СНИЛС/ОМС и анкету беременной
        await manager.start(RegistrationSG.snils_or_oms)
