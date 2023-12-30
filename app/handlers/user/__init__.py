from aiogram import Router


def get_user_router() -> Router:
    from . import info, start, file

    router = Router()
    router.include_router(info.router)
    router.include_router(start.router)
    router.include_router(file.router)

    return router
