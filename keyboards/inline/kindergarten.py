from gc import callbacks

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from loader import db

kindergarten_callback_query = CallbackData('kindergarten', 'number')


async def kindergarten_inline_button():
    markup = InlineKeyboardMarkup()
    for i in range(1, 22):
        callback_data = f"{i} - MTM"
        questionnaires = await db.select_questionnaires(kindergarten=callback_data)
        text_button = f"{callback_data} ({len(questionnaires)})"
        markup.insert(
            InlineKeyboardButton(
                text=text_button,
                callback_data=kindergarten_callback_query.new(number=callback_data)
            )
        )
    callback_data = "Betaraf/нейтрал"
    questionnaires = await db.select_questionnaires(kindergarten=callback_data)
    text_button = f"{callback_data} ({len(questionnaires)})"
    markup.insert(
        InlineKeyboardButton(
            text=text_button,
            callback_data=kindergarten_callback_query.new(number=callback_data)
        )
    )
    return markup
