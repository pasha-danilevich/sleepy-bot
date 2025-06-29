from dishka import make_async_container

from infrastructure.di.app import get_all_app_providers

container = make_async_container(*get_all_app_providers())
