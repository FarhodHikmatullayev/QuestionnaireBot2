from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.main_menu import main_menu_for_users, main_menu_for_admins
from loader import dp, db, bot


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
    stocks = await db.select_all_stocks()
    if stocks:
        stock = stocks[-1]
        message_id = stock['message_id']
        from_chat_id = stock['from_chat_id']
        await bot.forward_message(chat_id=message.from_user.id, from_chat_id=from_chat_id, message_id=message_id)
    if role == 'user':
        await message.answer(text=f"👋 Salom, Promo kodni olish uchun '🏷️ PromoCode' tugmasini bosing!",
                             reply_markup=main_menu_for_users)
    else:
        await message.answer(text=f"👋 Salom, Promo kodni tekshirish uchun promo kodni yuboring",
                             reply_markup=main_menu_for_admins)
