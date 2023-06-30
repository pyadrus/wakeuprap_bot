from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from system.dispatcher import dp, bot
from utils.database_init import connecting_database, creating_table_for_orders


class MakingAnOrder(StatesGroup):
    """Статусы заказа"""
    write_order_number = State()  # Обработчик ввода номера заказа
    write_name = State()  # Обработчик ввода наименования
    write_price = State()  # Обработчик ввода цены
    write_approximate_date = State()  # Обработчик ввода даты доставки


@dp.callback_query_handler(lambda c: c.data == "make_an_order")
async def order(callback_query: types.CallbackQuery, state: FSMContext):
    await state.reset_state()  # Сбрасываем состояние FSM (конечного автомата) к его начальному состоянию
    greeting_message = ("Привет! Я бот для сбора данных заказа.\n\n"
                        "Пожалуйста, введите номер 📦 заказа:")
    await bot.send_message(callback_query.from_user.id, greeting_message)
    await MakingAnOrder.write_order_number.set()  # Начальное состояние диалога с пользователем


@dp.message_handler(state=MakingAnOrder.write_order_number)
async def write_order_number(message: types.Message, state: FSMContext):
    """Обработчик ввода номера заказа"""
    order_number = message.text  # Сохранение значения переменной message.text в состоянии (state) с именем order_number
    await state.update_data(order_number=order_number)
    await MakingAnOrder.next()  # Переводим состояние FSM (конечный автомат) на следующее состояние
    await bot.send_message(message.from_user.id, "Пожалуйста, введите 📝 название:")


@dp.message_handler(state=MakingAnOrder.write_name)
async def write_name(message: types.Message, state: FSMContext):
    """Обработчик ввода наименования товара"""
    name = message.text  # Сохранение значения переменной message.text в состоянии (state) с именем name
    await state.update_data(name=name)
    await MakingAnOrder.next()  # Переводим состояние FSM (конечный автомат) на следующее состояние
    await bot.send_message(message.from_user.id, "Пожалуйста, введите 💸 стоимость с указанием валюты:")


@dp.message_handler(state=MakingAnOrder.write_price)
async def write_price(message: types.Message, state: FSMContext):
    """Обработчик ввода цены на товар"""
    price = message.text  # Сохранение значения переменной message.text в состоянии (state) с именем price
    await state.update_data(price=price)
    await MakingAnOrder.next()  # Переводим состояние FSM (конечный автомат) на следующее состояние
    await bot.send_message(message.from_user.id, "Пожалуйста, введите примерную 📆 дату доставки:")


@dp.message_handler(state=MakingAnOrder.write_approximate_date)
async def write_approximate_date(message: types.Message, state: FSMContext):
    """Обработчик ввода даты доставки и запись данных заказа в базу данных"""
    approximate_date = message.text
    await state.update_data(approximate_date=approximate_date)
    data = await state.get_data()  # Получение номера заказа
    # Извлечение данных из состояния
    order_number = data.get('order_number')  # Номер заказа
    name = data.get('name')  # Наименование заказа
    price = data.get('price')  # Стоимость заказа
    approximate_date = data.get('approximate_date')  # Примерная дата доставки заказа
    creating_table_for_orders()  # Создание таблицы для заказов
    conn, cursor = connecting_database()  # Подключение к базе данных SqLite
    # Сохранение данных в базу данных
    cursor.execute(
        "INSERT INTO orders (order_number, name, price, approximate_date) VALUES (?, ?, ?, ?)",
        (order_number, name, price, approximate_date))
    in_processing = 0  # Ожидается на складе
    sent = 0  # Заказ прибыл на склад и отправлен в Минск
    cancelled = 0  # Заказ прибыл на склад в Минске
    refund = 0  # Заказ получен
    cursor.execute(
        "INSERT INTO order_status (order_number, in_processing, sent, cancelled, refund) VALUES (?, ?, ?, ?, ?)",
        (order_number, in_processing, sent, cancelled, refund))
    conn.commit()  # Сохранение данных
    conn.close()  # Закрытие соединения
    await state.finish()

    order_details = (f"Заказ сформирован!\n\n"
                     f"📦 Номер заказа: {order_number}\n"
                     f"📝 Наименование заказа: {name}\n"
                     f"💸 Цена: {price}\n"
                     f"📆 Примерная дата доставки: {approximate_date}\n"
                     "\n\nДля возврата в начало нажмите /start")
    await bot.send_message(message.from_user.id, order_details, disable_web_page_preview=True)


def product_order_handler():
    """Регистрируем handlers для обработчиков сообщений"""
    dp.register_message_handler(order)
