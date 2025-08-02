from dishka import Provider, Scope, provide

from bot.dialogs.dreams.calendar.dialog import DreamsDialog
from bot.dialogs.home.dialog import HomeDialog
from bot.dialogs.start.dialog import StartDialog


class DialogProvider(Provider):
    scope = Scope.APP

    home = provide(HomeDialog)
    start = provide(StartDialog)
    dreams = provide(DreamsDialog)
