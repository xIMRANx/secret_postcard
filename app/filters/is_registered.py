from aiogram import types
from aiogram.filters import Filter

from app.db.functions import User


class IsRegistered(Filter):

    def __init__(self, is_registered: bool) -> None:
        self.is_registered = is_registered

    async def __call__(self, message: types.Message) -> bool:
        user = await User.is_registered(message.from_user.id)

        if not user:
            await message.answer(
                'Вы не зарегистрированы, введите команду /start'
            )

        return self.is_owner is True if user else False
