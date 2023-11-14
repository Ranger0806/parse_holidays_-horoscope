from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keybord import keybord_2_btns


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"*{message.from_user.first_name} Добро пожаловать!\nЭто бот праздников и гороскопов!*", reply_markup=keybord_2_btns(), parse_mode="Markdown")