from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject
from domain.dto.survey_dto import SurveyStatus
from domain.services.survey_service import SurveyService
from tg_bot.dialogs.survey_dialogs.surveys.daily import survey as daily_survey
from tg_bot.dialogs.user_dialogs.home.message_utils import (
    get_diary_button_text,
    get_diary_status_message,
    get_greeting_message,
)


@inject
async def get_data(service: FromDishka[SurveyService], **kwargs):
    manager: DialogManager = kwargs["dialog_manager"]
    survey_status: SurveyStatus = await service.get_survey_status(
        user_id=manager.event.from_user.id, survey=daily_survey
    )
    manager.dialog_data['session_in_progress'] = survey_status.session_in_progress
    diary_filled_today = survey_status.filled

    return {
        "greeting": get_greeting_message(),
        "survey_button_text": get_diary_button_text(
            diary_filled_today, survey_status.session_in_progress
        ),
        "diary_status": get_diary_status_message(diary_filled_today),
    }
