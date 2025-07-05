from dishka import Provider, Scope, provide

from bot.dialogs.home.dialog import HomeDialog
from bot.dialogs.record_dream.dialog import RecordDreamDialog
from bot.dialogs.start.dialog import StartDialog


class DialogProvider(Provider):
    scope = Scope.APP

    home = provide(HomeDialog)
    start = provide(StartDialog)
    record_dream = provide(RecordDreamDialog)
