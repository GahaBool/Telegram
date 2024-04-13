from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Информация о аккаунте"),
        ],
        {
            KeyboardButton(text="Меню: "),
            KeyboardButton(text="Донат: "),
        }
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?"
)
