import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from system.dispatcher import dp, bot


class AddingTrackNumber(StatesGroup):
    """Добавление номера заказа"""
    write_order_number = State()  # Обработчик ввода номера заказа
    result = State()  # Обработчик вывода результатов


@dp.callback_query_handler(lambda c: c.data == "add_track_number")
async def order(callback_query: types.CallbackQuery, state: FSMContext):
    await state.reset_state()  # Сброс состояния FSM (конечного автомата) к его начальному состоянию
    greeting_message = "Для добавления заказа введите его номер отслеживания. 📮"
    await bot.send_message(callback_query.from_user.id, greeting_message)
    await AddingTrackNumber.write_order_number.set()  # Начальное состояние диалога с пользователем


def get_order_status(order_number):
    conn = sqlite3.connect('setting/orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM order_status WHERE order_number = ?", (order_number,))
    result = cursor.fetchone()
    if result:
        _, in_processing, sent, cancelled, refund = result
        status = []
        if in_processing:
            status.append("Ожидается на складе")
        if sent:
            status.append("Заказ прибыл на склад и отправлен в Минск")
        if cancelled:
            status.append("Заказ прибыл на склад в Минске")
        if refund:
            status.append("Заказ получен")
        return status


@dp.message_handler(state=AddingTrackNumber.write_order_number)
async def write_order_number(message: types.Message, state: FSMContext):
    """Обработчик ввода номера заказа"""
    order_number = message.text  # Сохранение значения переменной message.text в состоянии (state) с именем order_number
    await state.update_data(order_number=order_number)
    conn = sqlite3.connect('setting/orders.db')  # Подключение к базе данных SQLite
    cursor = conn.cursor()  # Создание курсора для выполнения SQL-запросов
    # Выполнение SQL-запроса для извлечения данных
    cursor.execute("SELECT * FROM orders WHERE order_number = ?", (order_number,))
    row = cursor.fetchone()  # Извлечение строки данных из результата запроса
    if row:
        status_list = get_order_status(order_number)
        status_message = "\n".join(status_list) if status_list else "Статус неизвестен"
        order_details = (f"Заказ найден!\n\n"
                         f"📦 Номер заказа: {row[0]}\n"
                         f"📝 Наименование заказа: {row[1]}\n"
                         f"💸 Цена: {row[2]}\n"
                         f"📆 Примерная дата доставки: {row[3]}\n"
                         f"🔔 Статус: {status_message}\n"
                         "\n\nДля возврата в начало нажмите /start")
        await bot.send_message(message.from_user.id, order_details)
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS user_orders (user_id, order_number, name, price, approximate_date, status)""")
        cursor.execute(
            '''INSERT INTO user_orders (user_id, order_number, name, price, approximate_date, status) VALUES (?, ?, ?, ?, ?, ?)''',
            (message.from_user.id, order_number, row[1], row[2], row[3], status_message))
        conn.commit()
        dell_duplicate_order_number(order_number)
    else:
        await bot.send_message(message.from_user.id, "❌ Заказ с таким номером отслеживания не найден.")

    await state.finish()  # Завершение FSM (конечного автомата)


def dell_duplicate_order_number(order_number):
    """Удаление дубликатов из таблицы user_orders"""
    conn = sqlite3.connect('setting/orders.db')
    cursor = conn.cursor()
    # Удаление дубликатов из таблицы user_orders
    cursor.execute(
        "DELETE FROM user_orders WHERE rowid NOT IN (SELECT MIN(rowid) FROM user_orders GROUP BY user_id, order_number)")
    conn.commit()  # Применение изменений
    conn.close()  # Закрытие соединения с базой данных


def adding_track_number_handler():
    """Регистрируем handlers для обработчиков сообщений"""
    dp.register_message_handler(order, state="*")
    dp.register_message_handler(write_order_number, state=AddingTrackNumber.write_order_number)
