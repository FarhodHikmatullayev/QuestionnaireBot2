import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.misc import subscription
from loader import bot, db


class CheckSubscriptionMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            # if update.message.text in ['/start', '/help']:
            #     return
        elif update.callback_query:
            user = update.callback_query.from_user.id
        #     if update.callback_query.data == "check_subs":
        #         return
        # else:
        #     return

        result = f"Assalomu alaykum! Haftaning maxsus taklifi: {} uchun {}% chegirma. Promo-kod olish uchun sahifalarimizga obuna bo‘ling!"
        final_status = True
        channels = await db.select_all_channels()
        inline_keyboard = InlineKeyboardMarkup(row_width=1)
        for channel in channels:
            chat_id = int(channel['chat_id'])
            # chat_id = -4514999641
            status = await subscription.check(user_id=user,
                                              channel=chat_id)
            final_status *= status
            channel = await bot.get_chat(chat_id)
            if not status:
                invite_link = await channel.export_invite_link()
                button = InlineKeyboardButton(text=channel.title, url=invite_link)
                inline_keyboard.add(button)
                # result += (f"👉 <a href='{invite_link}'>{channel.title}</a>\n")

        if not final_status:
            await update.message.answer(result, reply_markup=inline_keyboard, disable_web_page_preview=True)
            raise CancelHandler()
