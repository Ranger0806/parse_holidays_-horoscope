from aiogram import Router, F
from aiogram.types import CallbackQuery
from bs4 import BeautifulSoup
import requests
from Config import array_zod
from keybord import keybord_2_btns


router = Router()

@router.callback_query(F.data == "horoskop")
async def horoskop(callback: CallbackQuery):
    stroka = ""
    await callback.message.delete()
    for url in array_zod[:7]:
        response = requests.get(url)
        bs = BeautifulSoup(response.text, "html.parser")
        cur1 = bs.find("h1")
        cur2 = bs.find('div', 'article__item article__item_alignment_left article__item_html')
        stroka += f"{cur1.text}\n{cur2.text}\n\n"
    await callback.message.answer(f"*{stroka}*", parse_mode="Markdown")
    stroka = ""
    for url in array_zod[7:]:
        response = requests.get(url)
        bs = BeautifulSoup(response.text, "html.parser")
        cur1 = bs.find("h1")
        cur2 = bs.find('div', 'article__item article__item_alignment_left article__item_html')
        stroka += f"{cur1.text}\n{cur2.text}\n\n"
    await callback.message.answer(f"*{stroka}*", reply_markup=keybord_2_btns(), parse_mode="Markdown")
    await callback.answer("Запрос выполнен!")
