from .mixins import *


class CRUDMixin(
    Create[CREAT_DTO, RESPONSE_PROTOCOL],
    Retrieve[RESPONSE_PROTOCOL],
    Update[UPDATE_DTO, RESPONSE_PROTOCOL],
    Delete,
    Generic[CREAT_DTO, RESPONSE_PROTOCOL, UPDATE_DTO],
):
    pass
