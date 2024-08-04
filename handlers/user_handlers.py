import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from system.dispatcher import dp, bot


class MakingAnOrder(StatesGroup):
    """Статусы заказа"""
    waiting_for_order_number = State()


@dp.callback_query_handler(lambda c: c.data == 'add_track_number')
async def check_order_start(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Пожалуйста, введите номер заказа:")
    # Переходим в состояние ожидания ввода номера заказа
    await MakingAnOrder.waiting_for_order_number.set()


# Подключение к базе данных SQLite
conn = sqlite3.connect('setting/orders.db')
cursor = conn.cursor()
# Создаем таблицу, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
                                                    first_name TEXT, last_name TEXT, username TEXT, date TEXT)''')
# Создаем таблицу order_status
cursor.execute('''CREATE TABLE IF NOT EXISTS order_status (order_number, in_processing, sent, cancelled,
                                                           refund)''')
conn.commit()


def get_order_status(order_number):
    cursor.execute("SELECT * FROM order_status WHERE order_number = ?", (order_number,))
    result = cursor.fetchone()
    if result:
        # Распаковываем значения из результата запроса
        order_number, in_processing, sent, cancelled, refund, completed = result
        # Формируем словарь со статусом заказа
        order_status = {'order_number': order_number, 'in_processing': in_processing, 'sent': sent,
                        'cancelled': cancelled, 'refund': refund}
        return order_status
    else:
        return None


# Обработчик ввода номера заказа
@dp.message_handler(state=MakingAnOrder.waiting_for_order_number)
async def check_order_status(message: types.Message, state: FSMContext):
    order_number = message.text
    # Получение статуса заказа по номеру
    order_status = get_order_status(order_number)
    if order_status:
        # Пользовательский заказ найден
        status_message = f"Статус вашего заказа ({order_number}):\n\n"
        if order_status['in_processing']:
            status_message += "Ожидается на складе\n"
        if order_status['sent']:
            status_message += "Заказ прибыл на склад и отправлен в Минск\n"
        if order_status['cancelled']:
            status_message += "Заказ прибыл на склад в Минске\n"
        if order_status['refund']:
            status_message += "Заказ получен\n"
        await message.reply(status_message)
    else:
        # Заказ с указанным номером не найден
        await message.reply("Заказ не найден.")
    # Завершаем состояние
    await state.finish()


def user_handler():
    """Регистрируем handlers для администратора"""
    dp.register_callback_query_handler(check_order_start)
