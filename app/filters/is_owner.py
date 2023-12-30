from aiogram import types
from aiogram.filters import Filter

from app.config import Config
from app.db.functions import User


class IsOwner(Filter):

    def __init__(self, is_owner: bool) -> None:
        self.is_owner = is_owner

    async def __call__(self, message: types.Message) -> bool:
        return self.is_owner is await User.is_admin(message.from_user.id)
