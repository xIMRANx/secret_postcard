from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True, generated=True)
    telegram_id = fields.BigIntField()
    name = fields.CharField(max_length=255)
    secret_name = fields.CharField(max_length=255, null=True)

    role = fields.CharField(max_length=255, null=True)


class Card(Model):
    id = fields.BigIntField(pk=True, generated=True)
    file_id = fields.CharField(max_length=255)
    description = fields.CharField(max_length=255, null=True)
    owner = fields.ForeignKeyField('models.User', related_name='cards', null=True)
