from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

get_promo_code_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏷️ PromoCode", callback_data='promo_code')
        ]
    ]
)
