from string import punctuation

from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f

user_group_router = Router()

restricted_words = {}

def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

@user_group_router.message(CommandStart())
async def start_cmd(message: types.Message):
    if restricted_words.intersection(message.text.lower().spplit()):
        await message.delete()