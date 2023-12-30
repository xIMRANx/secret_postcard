from aiogram import Router


def get_user_router() -> Router:
    from . import info, start

    router = Router()
    router.include_router(info.router)
    router.include_router(start.router)

    return router
