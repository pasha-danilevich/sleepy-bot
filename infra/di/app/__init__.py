from infra.di.app.providers import *


def get_all_app_providers() -> list[Provider]:
    return [
        ConfigProvider(),
    ]
