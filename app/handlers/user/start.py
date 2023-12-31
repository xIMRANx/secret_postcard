from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.db.functions import User
from app.keyboards.inline import get_instruction_keyboard
from app.config import Config
from aiogram_dialog import DialogManager

from random import choice
from app.dialogs.choice_anon import AnonDialog


router = Router()


@router.message(CommandStart())
async def cmd_start(
    message: Message, bot: Bot, config: Config, dialog_manager: DialogManager
):
    user_id = message.from_user.id
    chat_id = config.settings.chat_id

    await message.answer(choice(["❄️", "🎅"]))

    text = (
        "<b>Привет, если ты тут, значит хочешь участвовать в обмене открытками!</b>\n\n"
        "Что бы продолжить, ознакомься с инструкцией по кнопке ниже, "
        "выберите вариант анонимности и отправьте открытку с подписью."
    )

    await message.answer(
        text, reply_markup=get_instruction_keyboard(), parse_mode="HTML"
    )

    if not await User.is_registered(user_id):
        await User.register(user_id, message.from_user.full_name)

        await bot.send_message(chat_id, f"Новый пользователь! \n "
                                        f"<a href='tg://user?id={user_id}'>{message.from_user.full_name}</a>",
                               parse_mode="HTML")

        await dialog_manager.start(AnonDialog.choice)
