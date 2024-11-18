import random
import string
from datetime import timedelta, datetime

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

    stocks = await db.select_all_stocks()
    if not stocks:
        await message.answer(text="Aksiya mavjud emas")
        return
    stock = stocks[-1]
    created_at = stock['created_at'].date() + timedelta(days=3)
    today = datetime.now().date()
    if created_at < today:
        await message.answer(text="Aksiya mavjud emas")
        return

    promocodes = await db.select_promo_codes(user_id=user_id, stock_id=stock['id'])
    if promocodes:
        await message.answer(text="Sizda hozirgi aksiya uchun promocode mavjud")
        return

    promocode = generate_promo_code()
    code = await db.select_promo_code(code=promocode)
    while code:
        promocode = generate_promo_code()
        code = await db.select_promo_code(code=promocode)
    await db.create_promo_code(user_id=user_id, code=promocode, stock_id=stock['id'])
    await message.answer(text=f"🎉 Sizning promocodingiz: {promocode}")
