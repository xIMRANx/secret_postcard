from typing import Union

from tortoise.exceptions import DoesNotExist

from app.db import models

from datetime import datetime


class User(models.User):
    @classmethod
    async def is_registered(cls, telegram_id: int) -> Union[models.User, bool]:
        try:
            return await cls.get(telegram_id=telegram_id)
        except DoesNotExist:
            return False

    @classmethod
    async def is_admin(cls, telegram_id: int) -> bool:
        user = await cls.is_registered(telegram_id)
        if not user:
            return False

        if user.role == "admin":
            return True
        else:
            return False

    @classmethod
    async def register(cls, telegram_id: int, name: str = None) -> None:
        await User(
            telegram_id=telegram_id, name=name, create_date=datetime.now()
        ).save()

    @classmethod
    async def get_count(cls) -> int:
        return await cls.all().count()

    @classmethod
    async def edit_anonymous(cls, user_id: int, anonymous: bool) -> None:
        await cls.filter(telegram_id=user_id).update(anonymous=anonymous)

    @classmethod
    async def get_all_users(cls) -> list[models.User]:
        return await cls.all()


class Card(models.Card):
    @classmethod
    async def get_all_card_owners(cls) -> list[models.Card]:
        return await cls.filter(approved=True).values_list("owner_id", flat=True)

    @classmethod
    async def get_count(cls) -> int:
        return await cls.all().count()

    @classmethod
    async def create_card(
        cls, file_id: str, description: str, owner_id: int, file_type: str = "photo"
    ) -> None:
        await Card(
            file_id=file_id,
            description=description,
            owner_id=owner_id,
            file_type=file_type,
            create_date=datetime.now(),
        ).save()

    @classmethod
    async def check_exists(cls, user_id: int) -> bool:
        return await cls.filter(owner_id=user_id).exists()

    @classmethod
    async def approve(cls, user_id: int) -> None:
        await cls.filter(owner_id=user_id).update(approved=True)

    @classmethod
    async def get_card(cls, user_id: int) -> Union[models.Card, bool]:
        try:
            return await cls.get(owner_id=user_id, approved=False)
        except DoesNotExist:
            return False

    @classmethod
    async def delete_card(cls, user_id: int) -> None:
        await cls.filter(owner_id=user_id).delete()

    @classmethod
    async def get_all_cards(cls) -> list[models.Card]:
        return await cls.filter(approved=True).all()
