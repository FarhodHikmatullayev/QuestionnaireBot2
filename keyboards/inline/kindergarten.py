from gc import callbacks

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

kindergarten_callback_query = CallbackData('kindergarten', 'number')


async def kindergarten_inline_button():
    markup = InlineKeyboardMarkup()
    for i in range(1, 22):
        text_button = f"{i} - MTM"
        markup.insert(
            InlineKeyboardButton(
                text=text_button,
                callback_data=kindergarten_callback_query.new(number=text_button)
            )
        )
    text_button = "Betaraf/нейтрал"
    markup.insert(
        InlineKeyboardButton(
            text=text_button,
            callback_data=kindergarten_callback_query.new(number=text_button)
        )
    )
    return markup
