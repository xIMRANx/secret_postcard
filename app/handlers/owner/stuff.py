import time

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.filters.is_owner import IsOwner
from app.db.functions import User, Card

from random import choice

router = Router()


@router.message(IsOwner(is_owner=True), Command(commands=["ping"]))
async def ping_handler(message: Message):
    start = time.perf_counter_ns()
    reply_message = await message.answer("<code>⏱ Checking ping...</code>")
    end = time.perf_counter_ns()
    ping = (end - start) * 0.000001
    await reply_message.edit_text(
        f"<b>⏱ Ping -</b> <code>{round(ping, 3)}</code> <b>ms</b>"
    )


@router.message(IsOwner(is_owner=True), Command(commands=["send_postcard"]))
async def send_postcard_handler(message: Message):
    cards = await Card.get_all_cards()
    users = await User.get_all_users()

    for user in users:
        card = choice(cards)
        while card.owner_id == user.telegram_id:
            card = choice(cards)
        cards.remove(card)
        card_author = await User.is_registered(card.owner_id)
        card_author_name = 'Анонима' if card_author.anonymous else \
            f'<a href="tg://user?id={card.owner_id}">{card_author.name}</a>'
        card_description = f'<blockquote>{card.description}</blockquote>' if card.description else ''
        caption = f'''
        ✨ Вам открытка от {card_author_name}!

{card_description}
        '''

        match card.file_type:
            case 'photo':
                await message.bot.send_photo(user.telegram_id,
                                             card.file_id,
                                             caption=caption,
                                             parse_mode='HTML')
            case 'video':
                await message.bot.send_video(user.telegram_id,
                                              card.file_id,
                                              caption=caption,
                                              parse_mode='HTML')
            case 'animation':
                await message.bot.send_animation(user.telegram_id,
                                                  card.file_id,
                                                  caption=caption,
                                                  parse_mode='HTML')
