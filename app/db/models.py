from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True, generated=True)
    telegram_id = fields.BigIntField()
    name = fields.CharField(max_length=255)
    anonymous = fields.BooleanField(default=False)

    role = fields.CharField(max_length=255, default="user")


class Card(Model):
    id = fields.BigIntField(pk=True, generated=True)

    file_id = fields.CharField(max_length=255)
    file_type = fields.CharField(
        max_length=255, default="photo"
    )  # photo or video or animation

    description = fields.CharField(max_length=255, null=True)
    owner_id = fields.BigIntField()

    approved = fields.BooleanField(default=False)
