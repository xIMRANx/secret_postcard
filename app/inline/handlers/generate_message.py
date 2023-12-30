from aiogram import Router
from aiogram.types import InlineQuery

from app.inline.articles.get_message import get_message_article

router = Router()


@router.inline_query()
async def generate_message_query(inline_query: InlineQuery):
    await inline_query.answer(
        results=[get_message_article(inline_query.from_user)],
        cache_time=0,
        is_personal=True,
    )
