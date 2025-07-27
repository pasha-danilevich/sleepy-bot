from .mixins import *
from .types import RESPONSE_PROTOCOL


class CRUDMixin(
    Create[RESPONSE_PROTOCOL],
    Retrieve[RESPONSE_PROTOCOL],
    Update[RESPONSE_PROTOCOL],
    Delete,
    Generic[RESPONSE_PROTOCOL],
):
    pass
