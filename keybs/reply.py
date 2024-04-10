from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Информация о аккаунте"),
            KeyboardButton(text="Меню"),
            KeyboardButton(text="Донат: "),
        ],
    ],
)