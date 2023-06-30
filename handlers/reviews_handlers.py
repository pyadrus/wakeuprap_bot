from aiogram import types

from system.dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == 'reviews')
async def reviews_handlers(callback_query: types.CallbackQuery):
    """Отзывы от пользователей"""
    message_text_clothing = ("Тут будут ссылки на актуальные истории из Instagram.\n\n"
                             "👉 <a href='https://instagram.com/wakeuprap.by?igshid=NTc4MTIwNjQ2YQ=='>Instagram</a>"
                             "\n\nДля возврата в начало нажмите /start")
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, parse_mode=types.ParseMode.HTML)


def register_reviews_handler():
    """Регистрируем handlers для обработчиков сообщений"""
    dp.register_message_handler(reviews_handlers)
