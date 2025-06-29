from infrastructure.di.app.providers import ConfigProvider


def get_all_app_providers():
    return [
        ConfigProvider(),
    ]
