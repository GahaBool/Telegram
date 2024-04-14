from aiogram import F, types, Router
from aiogram.filters import Command, or_f
from filters.chat_types import ChatTypesFilter

from keybs import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(['private']))

@user_private_router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Hello", reply_markup=reply.start_kb)

@user_private_router.message(Command("information"))
async def start_cmd(message: types.Message):
    await message.answer(f"your information: {message.from_user}")

@user_private_router.message(or_f(Command("menu"), (F.text.lower().contains("меню"))))
async def start_cmd(message: types.Message):
    await message.answer("Меню: ")
@user_private_router.message(or_f(Command("donat"), (F.text.lower().contains("donat"))))
@user_private_router.message(Command("donat"))
async def start_cmd(message: types.Message):

    text = as_marked_section(
        Bold("Варианты доната:"),
        "Картой в боте",
        "При получении карта/кэш",
        "В заведении",
        marker=""
    )
    await message.answer(text.as_html)

@user_private_router.message(F.text.lower().contains("cipi"))
async def start_cmd(message: types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAEEXH9mBlUbKgNZ7VdNc4Ss4DhWAZn9DAAC3DoAAsTYgUhE2KXpN0MXpzQE")

