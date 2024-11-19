from aiogram import types

from loader import dp, bot


# Echo bot
@dp.message_handler(state=None, content_types=types.ContentTypes.ANY)
async def bot_echo(message: types.Message):
    await bot.forward_message(chat_id=message.from_user.id, from_chat_id=message.chat.id, message_id=message.message_id)
