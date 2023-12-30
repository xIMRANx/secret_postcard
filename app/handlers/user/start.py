from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.db.functions import User
from app.keyboards.inline import get_instruction_keyboard
from app.config import Config

from random import choice
from faker import Faker


fake = Faker("ru_RU")

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    user_id = message.from_user.id
    chat_id = Config.settings.chat_id

    await message.answer(choice(["❄️", "🎅"]))
    name = fake.name()

    text = (
        "<b>Привет, если ты тут, значит хочешь участвовать в обмене открытками!</b>\n\n"
        "Что бы продолжить, ознакомься с инструкцией по кнопке ниже "
        "и отправьте открытку с подписью."
    )

    if not await User.is_registered(user_id):
        await User.register(user_id, name)

        await bot.send_message(chat_id, f"Новый пользователь! {user_id}")

    await message.answer(
        text, reply_markup=get_instruction_keyboard(), parse_mode="HTML"
    )
