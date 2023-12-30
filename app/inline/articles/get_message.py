from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, User


def get_message_article(user: User):
    return InlineQueryResultArticle(
        id="message",
        title="123",
        description="123",
        input_message_content=InputTextMessageContent(
            message_text="<b>123</b>",
        ),
    )
