from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def text_handler(message: Message):
    """Text handler"""
    await message.answer("Открытка должна иметь фото, а не только текст!")
