from aiogram import Router


def get_inline_router() -> Router:
    from . import generate_message

    router = Router()
    router.include_router(generate_message.router)

    return router
