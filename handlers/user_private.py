from aiogram import types, Router
from aiogram.filters import Command

user_private_router = Router()

@user_private_router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(f"Hello {message.from_user.first_name}")

@user_private_router.message(Command("information"))
async def start_cmd(message: types.Message):
    await message.answer(f"your information: {message.from_user}")

@user_private_router.message(Command("donat"))
async def start_cmd(message: types.Message):
    await message.answer("Вариант доната:")

@user_private_router.message()
async def Message_User(message: types.Message):
    text = message.text

    for i in range(3):
        if text == "cipi cipi capa capa":
            await Bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEEXH9mBlUbKgNZ7VdNc4Ss4DhWAZn9DAAC3DoAAsTYgUhE2KXpN0MXpzQE")