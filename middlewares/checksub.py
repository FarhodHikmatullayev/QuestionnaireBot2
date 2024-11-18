import logging
from datetime import datetime, timedelta

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
        elif update.callback_query:
            user = update.callback_query.from_user.id

        stocks = await db.select_all_stocks()
        if stocks:
            stock = stocks[-1]
            created_at = stock['created_at'].date() + timedelta(days=3)
            today = datetime.now().date()
            if created_at >= today:
                result = f"✨ Assalomu alaykum! 🎉\n" \
                         f"🛍️ Haftaning maxsus taklifi: *{stock['title']}* uchun *{stock['stock_percent']}%* chegirma! 🎈\n" \
                         "📩 Promo-kod olish uchun sahifalarimizga obuna bo‘ling va yangiliklardan xabardor bo‘ling!"
            else:
                result = f"✨ Assalomu alaykum! 🎉\n" \
                         f"📩 Promo-kod olish uchun sahifalarimizga obuna bo‘ling va yangiliklardan xabardor bo‘ling!"
        else:
            result = f"✨ Assalomu alaykum! 🎉\n" \
                     f"📩 Promo-kod olish uchun sahifalarimizga obuna bo‘ling va yangiliklardan xabardor bo‘ling!"
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
        web_pages = await db.select_all_web_pages()
        for web_page in web_pages:
            invite_link = web_page['link']
            button = InlineKeyboardButton(text=web_page['title'], url=invite_link)
            inline_keyboard.add(button)


        if not final_status:
            await update.message.answer(result, reply_markup=inline_keyboard, disable_web_page_preview=True)
            raise CancelHandler()
