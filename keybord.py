from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def keybord_2_btns():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Гороскоп🔮", callback_data="horoskop"))
    builder.row(types.InlineKeyboardButton(text="Праздник🗓", callback_data="selebration"))
    return builder.as_markup()
