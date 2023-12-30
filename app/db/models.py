from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField()
    name = fields.CharField(max_length=255)
    anonymous = fields.BooleanField(default=False)

    role = fields.CharField(max_length=255, default="user")

    create_date = fields.CharField(max_length=255, default="0")


class Card(Model):
    id = fields.BigIntField(pk=True)

    file_id = fields.CharField(max_length=255)
    file_type = fields.CharField(
        max_length=255, default="photo"
    )  # photo or video or animation

    description = fields.CharField(max_length=512, null=True)
    owner_id = fields.BigIntField()

    approved = fields.BooleanField(default=False)

    create_date = fields.CharField(max_length=255, default="0")
