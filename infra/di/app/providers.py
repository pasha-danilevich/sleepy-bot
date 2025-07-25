from dishka import Provider, Scope, provide

from config import Config


class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    def get_config(self) -> Config:
        return Config()
