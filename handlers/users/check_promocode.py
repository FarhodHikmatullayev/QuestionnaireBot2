from datetime import timedelta, datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from setuptools.msvc import msvc14_get_vc_env

from loader import dp, db


@dp.message_handler(state='*')
async def check_promocode(message: types.Message, state: FSMContext):
    try:
        await state.finish()
    except:
        pass
    code = message.text
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
    user_role = user['role']
    if user_role != 'admin':
        return

    promocode = await db.select_promo_code(code=code)
    if not promocode:
        await message.answer(text="🚫 *Promo kod topilmadi*\n"
                                  "Iltimos, foydalangan promo kodni tekshirib ko'ring yoki yangi kodni sinab ko'ring.", parse_mode='Markdown')
        return
    is_active = promocode['is_active']
    stock_id = promocode['stock_id']
    stock = await db.select_stock(stock_id=stock_id)
    if not stock:
        await message.answer(text="🚫 *Promo kod topilmadi*\n"
                                  "Iltimos, foydalangan promo kodni tekshirib ko'ring yoki yangi kodni sinab ko'ring.", parse_mode='Markdown')
        return
    if not is_active:
        await message.answer(text="🚫 *Ilgari foydalanilgan*.\n"
                                  "Iltimos, yangi promo kod yoki boshqa imkoniyatlarni sinab ko'ring.", parse_mode='Markdown')
        return

    created_at = stock['created_at'].date() + timedelta(days=3)
    today = datetime.now().date()
    if created_at < today:
        await message.answer(text="⏳ *Promocod muddati o'tgan!*\n"
                                  "Iltimos, yangi promo kodni sinab ko'ring yoki aksiyalarimizdan foydalaning.",
                             parse_mode='Markdown')
        return

    await message.answer(text="✅ *Promocod muvaffaqiyatli ro'yxatga olindi!*\n"
                              "🎉 Iltimos, bu kodni aksiyalarda foydalaning va chegirmalardan bahramand bo'ling!",
                         parse_mode='Markdown')
    await db.update_promo_code(promo_code_id=promocode['id'], is_active=False)
