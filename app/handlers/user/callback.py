from aiogram import Bot, Router
from aiogram.types import CallbackQuery
from app.db.functions import Card

router = Router()


@router.callback_query()
async def approve_handler(query: CallbackQuery, bot: Bot):
    if ":" not in query.data:
        return

    action, user_id = query.data.split(":")
    card = await Card.get_card(user_id)

    if not card:
        return

    if action == "approve":
        await Card.approve(user_id)
        await bot.send_message(user_id, "Ваша открытка одобрена!")
        await query.message.edit_caption(
            caption=query.message.caption + "\n\n<b>✅ Одобрено</b>"
        )
    elif action == "decline":
        await bot.send_message(user_id, "Ваша открытка отклонена!\nНо вы можете попробовать еще раз!")
        await Card.delete_card(user_id)
        await query.message.edit_caption(
            caption=query.message.caption + "\n\n<b>❌ Отклонено </b>"
        )