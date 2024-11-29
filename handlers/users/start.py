from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.main_menu import main_menu_for_admins
from keyboards.inline.kindergarten import kindergarten_inline_button
from loader import dp, db, bot


@dp.callback_query_handler(text="check", state="*")
async def bot_start(call: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()
    except:
        pass
    user_telegram_id = call.from_user.id
    users = await db.select_users(telegram_id=user_telegram_id)
    if not users:
        full_name = call.from_user.full_name
        username = call.from_user.username
        user = await db.create_user(
            username=username,
            full_name=full_name,
            telegram_id=user_telegram_id
        )
        role = user['role']
    else:
        user = users[0]
        role = user['role']

    if role == 'user':
        markup = await kindergarten_inline_button()
        await call.message.edit_text(text=f"👋 Salom, quyidagi maktabgacha ta'lim muassalaridan birini tanlang:",
                                     reply_markup=markup)
    else:
        await call.message.answer(
            text=f"👋 Salom, so'rovnoma natijalarini yuklab olish uchun 'Download' tugmasini bosing",
            reply_markup=main_menu_for_admins)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


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

    if role == 'user':
        markup = await kindergarten_inline_button()
        await message.answer(text=f"👋 Salom, quyidagi maktabgacha ta'lim muassalaridan birini tanlang:",
                             reply_markup=markup)
    else:
        await message.answer(text=f"👋 Salom, so'rovnoma natijalarini yuklab olish uchun 'Download' tugmasini bosing",
                             reply_markup=main_menu_for_admins)
