from tortoise.expressions import Q
from tortoise.manager import Manager
from tortoise.queryset import QuerySet


class ActiveManager(Manager):
    def get_queryset(self) -> QuerySet:
        return (
            super(ActiveManager, self)
            .get_queryset()
            .filter(Q(active=True, deleted=False, join_type='AND'))
        )
