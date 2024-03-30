import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router

Bot = Bot(os.getenv('Token'))
dp = Dispatcher()

dp.include_router(user_private_router)

async def main():
    await Bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(Bot)

asyncio.run(main())