from aiogram import Bot, Dispatcher
import asyncio
import logging
from Config import BOT_TOKEN
import horoskop_handler
import start
import selebr_handler


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(start.router, horoskop_handler.router, selebr_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

