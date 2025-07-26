from infra.di.bot.dialogs.dialogs import *


def get_all_bot_providers() -> list[Provider]:
    return [DialogProvider()]
