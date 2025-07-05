from dishka import Provider, Scope, provide

from bot.dialogs.home.dialog import HomeDialog



class DialogProvider(Provider):
    scope = Scope.APP

    home = provide(HomeDialog)
