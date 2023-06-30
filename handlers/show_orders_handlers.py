import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.add_track_number_handlers import get_order_status
from system.dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == "my_order")
async def my_order(callback_query: types.CallbackQuery, state: FSMContext):
    await state.reset_state()  # Сброс состояния FSM (конечного автомата) к его начальному состоянию
    # Подключение к базе данных SQLite
    conn = sqlite3.connect('setting/orders.db')
    # Создание курсора для выполнения SQL-запросов
    cursor = conn.cursor()
    # Выполнение SQL-запроса для извлечения данных
    cursor.execute("SELECT * FROM user_orders WHERE user_id = ?", (callback_query.from_user.id,))
    # Извлечение строк данных из результата запроса
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            # dell_duplicate_order_number(row[1])
            status_list = get_order_status(row[1])
            status_message = "\n".join(status_list) if status_list else "Статус неизвестен"
            order_details = (f"📦 Номер заказа: {row[1]}\n"
                             f"📝 Наименование заказа: {row[2]}\n"
                             f"💸 Цена: {row[3]}\n"
                             f"📆 Примерная дата доставки: {row[4]}\n"
                             f"🔔 Статус: {status_message}\n"
                             "\n\nДля возврата в начало нажмите /start")
            await bot.send_message(callback_query.from_user.id, order_details)
    else:
        await bot.send_message(callback_query.from_user.id, "У вас нет заказов")


def my_order_handler():
    """Регистрируем handlers для обработчиков сообщений"""
    dp.register_message_handler(my_order)
