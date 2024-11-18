from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.main_menu import main_menu_for_users, main_menu_for_admins
from loader import dp, db


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
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
        role = user['role']
    else:
        user = users[0]
        role = user['role']
    if role == 'admin':
        await message.answer(f"👋 Salom, Promo kodni olish uchun '🏷️ PromoCode' tugmasini bosing!",
                             reply_markup=main_menu_for_users)
    else:
        await message.answer(f"👋 Salom, Promo kodni tekshirish uchun '🔑 PromoCodni tekshirish' tugmasini bosing!",
                             reply_markup=main_menu_for_admins)
