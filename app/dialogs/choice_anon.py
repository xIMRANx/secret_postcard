from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from app.db.functions import User
from typing import Any


class AnonDialog(StatesGroup):
    choice = State()


async def action(type_: str, user_id: int) -> None:
    user = await User.is_registered(user_id)

    if not user:
        return

    await User.edit_anonymous(user_id, type_ == "anon")
    return


async def click_anon(c: CallbackQuery, _: Any, manager: DialogManager) -> None:
    c.answer("Вы выбрали анонимность")
    await action("anon", c.from_user.id)
    await c.message.delete()
    await manager.done()


async def click_show(c: CallbackQuery, _: Any, manager: DialogManager) -> None:
    c.answer("Вы выбрали показывать имя")
    await action("show", c.from_user.id)
    await c.message.delete()
    await manager.done()


ui = Dialog(
    Window(
        Const("<b>Выберите (перевыбрать будет нельзя): </b>"),
        Button(Const("Остаться анонимным"), id="anon", on_click=click_anon),
        Button(Const("Показать ваше имя в открытке"), id="show", on_click=click_show),
        state=AnonDialog.choice,
    ),
)
