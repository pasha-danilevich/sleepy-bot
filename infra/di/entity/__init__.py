from .providers import *


def get_all_entity_providers() -> list[Provider]:
    return [UserProvider()]
