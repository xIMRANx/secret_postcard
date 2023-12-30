from aiogram import Router, Bot, F
from aiogram.types import Message

from app.db.functions import User
from app.db.functions import Card
from app.keyboards.inline import get_approve_keyboard
from app.config import Config

router = Router()


@router.message(F.content_type.in_({"photo", "video", "animation"}))
async def get_postcard(message: Message, bot: Bot, config: Config):
    if await Card.check_exists(message.from_user.id):
        await message.answer("Вы уже отправили свою открытку!")
        return

    postcard_type = message.content_type
    if message.photo is not None:
        file_id = message.photo[-1].file_id
    elif message.video is not None:
        file_id = message.video.file_id
    elif message.animation is not None:
        file_id = message.animation.file_id
    else:
        file_id = None

    user_id = message.from_user.id
    chat_id = config.settings.chat_id
    if not await User.is_registered(user_id):
        await message.answer(
            "<b>Уупс, произошла ошибка</b>"
            "\n\n"
            "Похоже, что вы не зарегистрированы в системе."
            "Попробуйте перезапустить бота командой /start"
        )

    caption = message.caption
    text = f'<b>Новая открытка</b> от <a href="tg://user?id={user_id}">{user_id}</a>\n\nОписание: {str(caption)}'

    match postcard_type:
        case "photo":
            await bot.send_photo(
                chat_id,
                file_id,
                caption=text,
                parse_mode="HTML",
                reply_markup=get_approve_keyboard(user_id),
            )
        case "video":
            await bot.send_video(
                chat_id,
                file_id,
                caption=text,
                parse_mode="HTML",
                reply_markup=get_approve_keyboard(user_id),
            )
        case "animation":
            await bot.send_animation(
                chat_id,
                file_id,
                caption=text,
                parse_mode="HTML",
                reply_markup=get_approve_keyboard(user_id),
            )

    await Card.create_card(
        file_id=file_id,
        description=caption,
        owner_id=user_id,
        file_type=postcard_type,
    )

    await message.answer(
        "Открытка отправлена на проверку.\n" "После проверки вы получите уведомление."
    )
