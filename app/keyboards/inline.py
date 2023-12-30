from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_author_keyboard(owner_id):
    buttons = [
        [InlineKeyboardButton(text="Автор", url=f"tg://user?id={owner_id}")],
    ]
    keyboard = InlineKeyboardBuilder(markup=buttons)
    return keyboard.as_markup()


def get_instruction_keyboard():
    buttons = [[InlineKeyboardButton(text="Инструкция", url=f"https://google.com")]]
    keyboard = InlineKeyboardBuilder(markup=buttons)
    return keyboard.as_markup()