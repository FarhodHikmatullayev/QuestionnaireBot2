from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.kindergarten import kindergarten_callback_query
from loader import dp, db, bot


@dp.callback_query_handler(kindergarten_callback_query.filter(), state="*")
async def get_branch(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    try:
        await state.finish()
    except:
        pass

    user_telegram_id = call.from_user.id
    users = await db.select_users(telegram_id=user_telegram_id)
    if users:
        user_id = users[0]['id']
        await state.update_data(user_id=user_id)
    else:
        username = call.from_user.username
        full_name = call.from_user.full_name
        user = await db.create_user(
            username=username,
            full_name=full_name,
            telegram_id=user_telegram_id,
        )
        user_id = user['id']
        await state.update_data(user_id=user_id)

    await call.message.edit_text(text="✅ Ovoz berish jarayoni yakunlandi!\n"
                                      "🙏 Ishtirokingiz uchun katta rahmat.")
    return

    questionnaires = await db.select_questionnaires(user_id=user_id)
    if questionnaires:
        await call.message.edit_text(text="⚠️ Siz ilgari so'rovnomaga javob yuborgansiz.")
        return

    questionnaire = await db.create_questionnaire(
        user_id=user_id,
        kindergarten=callback_data.get('number')
    )
    await call.message.edit_text(text="✅ Javobingiz saqlandi")
