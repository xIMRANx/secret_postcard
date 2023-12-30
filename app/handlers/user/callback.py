from aiogram import Bot, Router
from aiogram.types import CallbackQuery
from app.db.functions import User, Card

router = Router()


@router.callback_query()
async def approve_handler(query: CallbackQuery, bot: Bot):
    pass
