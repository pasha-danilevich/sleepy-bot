from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from infra.db.tables.active_manager import ActiveManager
from infra.db.tables.base_mixin import BaseTableMixin


class User(BaseTableMixin):
    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=128, null=True)
    fullname = fields.CharField(max_length=128, null=True)
    birthday = fields.DateField(null=True)
    age = fields.IntField(null=True)
    gender = fields.IntField(null=True)
    phone = fields.CharField(max_length=20, null=True)
    email = fields.CharField(max_length=128, null=True)

    class Meta:
        table = 'user'
        table_description = 'Пользователи телеграмм бота'
        manager = ActiveManager()

    def __str__(self):
        return f'<User: {self.id} - {self.username}>'


UserPydantic = pydantic_model_creator(User)
