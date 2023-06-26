# Импортируем модуль для работы с базой данных SQLite
import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from system.dispatcher import dp, bot
from utils.database_init import connecting_database, creating_table_for_orders


# Создание класса состояний
class MakingAnOrder(StatesGroup):
    making_an_order = State()
    write_name = State()
    write_phone = State()
    write_link = State()
    write_size = State()
    write_color = State()
    write_price = State()


@dp.callback_query_handler(lambda c: c.data == "make_an_order")
async def order(callback_query: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    greeting_post_on = ("Привет! Я бот для сбора данных заказа.\n\n"
                        "Пожалуйста, введите ваше имя:")
    await bot.send_message(callback_query.from_user.id, greeting_post_on)
    await MakingAnOrder.write_name.set()


# Обработчик ввода имени
@dp.message_handler(state=MakingAnOrder.write_name)
async def write_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await MakingAnOrder.next()
    await bot.send_message(message.from_user.id, "Пожалуйста, введите ваш номер телефона:")


# Обработчик номера телефона
@dp.message_handler(state=MakingAnOrder.write_phone)
async def write_phone(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data(phone=phone)
    await MakingAnOrder.next()
    linc = f"Пожалуйста, введите ссылку на товар:"
    await bot.send_message(message.from_user.id, linc, disable_web_page_preview=True, parse_mode=types.ParseMode.HTML)


# Обработчик ввода ссылки на товар
@dp.message_handler(state=MakingAnOrder.write_link)
async def write_link(message: types.Message, state: FSMContext):
    link = message.text
    await state.update_data(link=link)
    await MakingAnOrder.next()
    await bot.send_message(message.from_user.id, "Пожалуйста, введите размер товара:")


# Обработчик ввода размера товара
@dp.message_handler(state=MakingAnOrder.write_size)
async def write_size(message: types.Message, state: FSMContext):
    size = message.text
    await state.update_data(size=size)
    await MakingAnOrder.next()
    await bot.send_message(message.from_user.id, "Пожалуйста, введите цвет товара:")


# Обработчик ввода цвета товара
@dp.message_handler(state=MakingAnOrder.write_color)
async def write_color(message: types.Message, state: FSMContext):
    color = message.text
    await state.update_data(color=color)
    await MakingAnOrder.next()
    await bot.send_message(message.from_user.id, "Пожалуйста, введите цену товара:")


# Обработчик ввода цены товара
@dp.message_handler(state=MakingAnOrder.write_price)
async def write_price(message: types.Message, state: FSMContext):
    price = message.text
    await state.update_data(price=price)
    # Получение текущей даты
    dat = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = await state.get_data()
    # Извлечение данных из состояния
    user_id = message.from_user.id
    name = data.get('name')
    phone = data.get('phone')
    link = data.get('link')
    size = data.get('size')
    color = data.get('color')
    price = data.get('price')
    current_time = datetime.datetime.now().strftime("%d%Y%H%M")
    order_number = f"{user_id}{current_time}"
    creating_table_for_orders()  # Создание таблицы для заказов
    conn, cursor = connecting_database()
    # Сохранение данных в базу данных
    cursor.execute("INSERT INTO orders "
                   "(user_id, name, phone, link, size, color, price, order_number, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (user_id, name, phone, link, size, color, price, order_number, dat))
    in_processing = None
    sent = None
    cancelled = None
    refund = None
    completed = None
    # Обновляем соответствующий статус заказа в базе данных
    cursor.execute("INSERT INTO order_status (order_number, in_processing, sent, cancelled, refund, completed) "
                   "VALUES (?, ?, ?, ?, ?, ?)",
                   (order_number, in_processing, sent, cancelled, refund, completed))

    conn.commit()
    await state.finish()

    order_details = (f"Спасибо за ваш заказ!\n\n"
                     f"Данные заказа были отправлены нашему менеджеру\n\n"
                     f""f"Имя: {name}\n"
                     f"Номер телефона: {phone}\n"
                     f"Ссылка на товар: {link}\n"
                     f"Размер: {size}\n"
                     f"Цвет: {color}\n"
                     f"Цена: {price}\n"
                     f"Номер заказа: {str(user_id) + str(current_time)}"
                     "\n\nДля возврата в начало нажмите /start")
    await bot.send_message(message.from_user.id, order_details, disable_web_page_preview=True)

    # Определение данных о пользователе для отправки администратору
    user = message.from_user
    user_info = f"{user.first_name} "
    if user.last_name:
        user_info += f"{user.last_name} "
    if user.username:
        user_info += f"@{user.username}\n"

    # admin_id = 5958542955  # Poizon менеджер
    # admin_id = 5837917794  # @PyAdminRUS
    admin_id = 1062323239  # @vitalure
    order_details_admin = (f"Заказ от: {user_info}\n"
                           f"Номер телефона: {phone}\n"
                           f"Ссылка на товар: {link}\n"
                           f"Размер: {size}\n"
                           f"Цвет: {color}\n"
                           f"Цена: {price}\n"
                           f"Номер заказа: {str(user_id) + str(current_time)}")
    await bot.send_message(admin_id, order_details_admin, disable_web_page_preview=True)


def product_order_handler():
    dp.register_message_handler(order)
