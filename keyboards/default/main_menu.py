from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_for_admins = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Download"),
        ],
    ]
)
