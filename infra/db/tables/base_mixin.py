from tortoise import fields, models


class ActualMixin:
    active = fields.BooleanField(default=True)
    deleted = fields.BooleanField(default=False)


class TimestampMixin:
    """
    Миксин для автоматического управления датами создания и обновления
    """

    created_at = fields.DatetimeField(
        auto_now_add=True, description="Дата и время создания записи", null=False
    )
    updated_at = fields.DatetimeField(
        auto_now=True,
        description="Дата и время последнего обновления записи",
        null=False,
    )


class BaseTableMixin(models.Model, TimestampMixin, ActualMixin):
    pass
