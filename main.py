import asyncio
import os

from aiogram import Bot, Dispatcher, types


from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from common.bot_command_list import private

Bot = Bot(os.getenv('Token'))
dp = Dispatcher()

dp.include_router(user_private_router)

async def main():
    await Bot.delete_webhook(drop_pending_updates=True)
    await Bot.setBotCommands(scope=botCommandScopeDefault, commands=private)
    await dp.start_polling(Bot)

asyncio.run(main())