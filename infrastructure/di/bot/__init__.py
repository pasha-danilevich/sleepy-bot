from infrastructure.di.bot.dialogs.dialogs import DialogProvider


def get_all_bot_providers():
    return [DialogProvider()]