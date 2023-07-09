from aiogram import types

from messages.reviews_text import message_text_clothing
from system.dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == 'reviews')
async def reviews_handlers(callback_query: types.CallbackQuery):
    """Отзывы от пользователей"""

    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, parse_mode=types.ParseMode.HTML)


def register_reviews_handler():
    """Регистрируем handlers для обработчиков сообщений"""
    dp.register_message_handler(reviews_handlers)
