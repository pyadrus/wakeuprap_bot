from aiogram import types

from system.dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == 'make_an_order_user')
async def make_order_user_handlers(callback_query: types.CallbackQuery):
    """Ответы от пользователей"""
    message_text_clothing = ("Определились с выбором? Отлично!\n\n"
                             "Чтобы сделать заказ – напишите менеджеру: @wakeuplogistic"
                             "\n\nДля возврата в начало нажмите /start")
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, parse_mode=types.ParseMode.HTML)


def register_make_order_user_handlers():
    """Регистрируем handlers для обработчиков сообщений"""
    dp.register_message_handler(make_order_user_handlers)
