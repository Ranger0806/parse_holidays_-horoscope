from aiogram import Router, F
from aiogram.types import CallbackQuery
from bs4 import BeautifulSoup
import requests
from Config import selebr_link
from keybord import keybord_2_btns


router = Router()


@router.callback_query(F.data == "selebration")
async def selebration(callback: CallbackQuery):
    stroka = "Праздники сегодня:\n"
    response = requests.get(selebr_link)
    bs = BeautifulSoup(response.text, "html.parser")
    cur2 = bs.find_all("span", "cl")
    for ell in cur2:
        stroka += ell.text
    await callback.message.answer(f"*{stroka}*", reply_markup=keybord_2_btns(), parse_mode="Markdown")
    await callback.answer("Запрос выполнен!")
