import random
import string

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db


def generate_promo_code(length=8):
    characters = string.ascii_uppercase + string.digits
    promo_code = ''.join(random.choices(characters, k=length))
    return promo_code


@dp.message_handler(text="🏷️ PromoCode", state='*')
async def create_promocode(message: types.Message, state: FSMContext):
    try:
        await state.finish()
    except:
        pass
    user_telegram_id = message.from_user.id
    users = await db.select_users(telegram_id=user_telegram_id)
    if not users:
        full_name = message.from_user.full_name
        username = message.from_user.username
        user = await db.create_user(
            username=username,
            full_name=full_name,
            telegram_id=user_telegram_id
        )

    else:
        user = users[0]
    user_id = user['id']

    promocode = generate_promo_code()
    code = await db.select_promo_code(code=promocode)
    while code:
        promocode = generate_promo_code()
        code = await db.select_promo_code(code=promocode)
    await db.create_promo_code(user_id=user_id, code=promocode)
    await message.answer(text=f"🎉 Sizning promocodingiz: {promocode}")
