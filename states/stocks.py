from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateStockState(StatesGroup):
    from_chat_id = State()
    message_id = State()