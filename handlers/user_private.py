from aiogram import F, types, Router
from aiogram.filters import Command, or_f
from filters.chat_types import ChatTypesFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(['private']))

@user_private_router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(f"Hello {message.from_user.first_name}")

@user_private_router.message(Command("information"))
async def start_cmd(message: types.Message):
    await message.answer(f"your information: {message.from_user}")

@user_private_router.message(or_f(Command("menu"), (F.text.lower().contains("меню"))))
async def start_cmd(message: types.Message):
    await message.answer("Меню: ")

@user_private_router.message(Command("donat"))
async def start_cmd(message: types.Message):
    await message.answer("Вариант доната:")

@user_private_router.message(F.text.lower().contains("cipi"))
async def start_cmd(message: types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAEEXH9mBlUbKgNZ7VdNc4Ss4DhWAZn9DAAC3DoAAsTYgUhE2KXpN0MXpzQE")

