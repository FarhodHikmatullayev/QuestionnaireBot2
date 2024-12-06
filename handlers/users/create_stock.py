from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.confirmation import confirm_keyboard
from loader import dp, bot, db
from states.stocks import CreateStockState


@dp.callback_query_handler(state=CreateStockState.from_chat_id, text="no")
async def cancel_saving_stock(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text="❌ Saqlash bekor qilindi")
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await state.finish()


@dp.callback_query_handler(state=CreateStockState.from_chat_id, text='yes')
async def confirm_saving_stock(call: types.CallbackQuery, state: FSMContext):
    users = await db.select_all_users()
    data = await state.get_data()
    from_chat_id = data.get('from_chat_id')
    message_id = data.get('message_id')
    await db.create_stock(from_chat_id=from_chat_id, message_id=message_id)
    await call.message.answer(text="✅ Yaratildi")

    for user in users:
        try:
            await bot.forward_message(chat_id=user['telegram_id'], from_chat_id=from_chat_id, message_id=message_id)
        except:
            pass

    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await state.finish()


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def start_confirmation_function(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    users = await db.select_users(telegram_id=telegram_id)
    if not users:
        full_name = message.from_user.full_name
        username = message.from_user.username
        user = await db.create_user(
            username=username,
            full_name=full_name,
            telegram_id=telegram_id
        )
        role = user['role']
    else:
        user = users[0]
        role = user['role']

    if role == 'user':
        return
    await CreateStockState.from_chat_id.set()
    from_chat_id = message.chat.id
    message_id = message.message_id
    await state.update_data(
        from_chat_id=from_chat_id,
        message_id=message_id
    )
    data = await state.get_data()
    from_chat_id = data.get('from_chat_id')
    message_id = data.get('message_id')
    await bot.forward_message(chat_id=message.from_user.id, from_chat_id=from_chat_id, message_id=message_id)
    await message.answer(
        text="📝 Sizning aksiya e'loningiz foydalanuvchilargan mana shunday ko'rinadi, saqlashni xohlaysizmi?",
        reply_markup=confirm_keyboard)
