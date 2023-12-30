from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_author_keyboard(owner_id):
    buttons = [
        [InlineKeyboardButton(text="Автор", url=f"tg://user?id={owner_id}")],
    ]
    keyboard = InlineKeyboardBuilder(markup=buttons)
    return keyboard.as_markup()


def get_instruction_keyboard():
    buttons = [
        [
            InlineKeyboardButton(
                text="Инструкция",
                url="https://telegra.ph/Instrukciya-k-botu-Tajnyj-Santa-12-30",
            )
        ]
    ]
    keyboard = InlineKeyboardBuilder(markup=buttons)
    return keyboard.as_markup()


def get_approve_keyboard(user_id):
    buttons = [
        [InlineKeyboardButton(text="✅", callback_data=f"approve:{user_id}")],
        [InlineKeyboardButton(text="❌", callback_data=f"decline:{user_id}")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)
    return keyboard.as_markup()
