import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F, Router

from src.utils.commands import set_commands

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()


async def start_bot(bot: Bot):
    """
    Уведомление о запуске админу
    """
    await bot.send_message(chat_id=os.getenv("ADMIN_ID"), text="Бот запущен!")


async def main():
    await set_commands(bot)
    await start_bot(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
