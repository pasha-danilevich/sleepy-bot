from tortoise import fields

from infra.db.tables.base_mixin import BaseTableMixin


class SleepRecord(BaseTableMixin):
    id = fields.BigIntField(pk=True)
    user = fields.ForeignKeyField('models.User')  # type: ignore[var-annotated]
    bedtime = fields.DatetimeField()  # Время отхода ко сну
    wakeup_time = fields.DatetimeField(null=True)  # Время пробуждения
    dream_text = fields.TextField(null=True)  # Текст сновидения
    sleep_score = fields.IntField(  # Оценка сна
        null=True, description="Оценка качества сна (1-5)"  # Необязательное поле
    )

    class Meta:
        table = "sleeprecord"  # Название таблицы в БД
        indexes = ("user_id",)  # Индекс для быстрого поиска по user_id

    def __str__(self) -> str:
        return f"Сон пользователя {self.user.id} от {self.bedtime.date()}"
