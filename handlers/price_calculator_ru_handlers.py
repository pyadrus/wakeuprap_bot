import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.delivery_keyboard import delivery_keyboard_technics_ru, \
    product_category_by_russia_polish_zloty_ru_keyboard, product_category_by_russia_euro_ru_keyboard, \
    product_category_by_russia_yuan_ru_keyboard
from messages.message_text_calculate import message_text_price_polish_zloty, message_text_price_euro, \
    message_text_price_yuan
from system.dispatcher import dp, bot, DELIVERY_RU_EUR, DELIVERY_RU_YUAN_ACCESSORIES, \
    DELIVERY_RU_YUAN_SHOES, COMMISSION_RU_YUAN_SHOES, DELIVERY_RU_YUAN_CLOTHING, \
    COMMISSION_RU_YUAN_CLOTHING, COMMISSION_RU_EUR, COMMISSION_RU_YUAN_ACCESSORIES


def get_currencies():
    """Получение списка валют"""
    conn = sqlite3.connect('setting/orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM currencies")
    row = cursor.fetchone()
    return row


class TechStateAcceleratedByTruck(StatesGroup):
    """Расчет стоимости доставки"""
    price_yuan_ru = State()
    price_yuan_ru_accessories = State()
    price_shoes_ru_yuan = State()
    price_clothing_ru_yuan = State()


@dp.callback_query_handler(lambda c: c.data == 'russia')
async def calculate_cost_handler(callback_query: types.CallbackQuery):
    """Насчитать стоимость доставки в зависимости от страны и типа валюты"""
    technics_delivery_keyboard = delivery_keyboard_technics_ru()
    message_text_clothing = "Вы выбрали 🇷🇺 Россия.\n\nВыберите валюту."
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=technics_delivery_keyboard,
                           parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == 'polish_zloty_ru')
async def calculate_cost_handler(callback_query: types.CallbackQuery):
    """Насчитать стоимость доставки в зависимости от страны и типа валюты"""
    product_category_keyboard = product_category_by_russia_polish_zloty_ru_keyboard()
    message_text_clothing = "Вы выбрали Польский злотый.\n\nВыберите категорию товара."
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=product_category_keyboard,
                           parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == 'accessories_ru_polish_zloty')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в польских злотых"""
    await bot.send_message(callback_query.from_user.id, message_text_price_polish_zloty,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        polish_zloty_ru = row[4]  # Курс Польского злотого к Русскому рублю
        await state.update_data(shipping_cost=polish_zloty_ru)


@dp.callback_query_handler(lambda c: c.data == 'shoes_ru_polish_zloty')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в польских злотых"""
    await bot.send_message(callback_query.from_user.id, message_text_price_polish_zloty,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        polish_zloty_ru = row[4]  # Курс Польского злотого к Русскому рублю
        await state.update_data(shipping_cost=polish_zloty_ru)


@dp.callback_query_handler(lambda c: c.data == 'clothing_ru_polish_zloty')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в польских злотых"""
    await bot.send_message(callback_query.from_user.id, message_text_price_polish_zloty,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        polish_zloty_ru = row[4]  # Курс Польского злотого к Русскому рублю
        await state.update_data(shipping_cost=polish_zloty_ru)


@dp.callback_query_handler(lambda c: c.data == 'euro_ru')
async def calculate_cost_handler(callback_query: types.CallbackQuery):
    """Насчитать стоимость доставки в зависимости от страны и типа валюты"""
    product_category_keyboard = product_category_by_russia_euro_ru_keyboard()
    message_text_clothing = "Вы выбрали Евро.\n\nВыберите категорию товара."
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=product_category_keyboard,
                           parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == 'accessories_ru_euro')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в евро"""
    await bot.send_message(callback_query.from_user.id, message_text_price_euro,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        euro_ru = row[5]  # Курс Евро к Русскому рублю
        await state.update_data(shipping_cost=euro_ru)


@dp.callback_query_handler(lambda c: c.data == 'shoes_ru_euro')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в евро"""
    await bot.send_message(callback_query.from_user.id, message_text_price_euro,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        euro_ru = row[5]  # Курс Евро к Русскому рублю
        await state.update_data(shipping_cost=euro_ru)


@dp.callback_query_handler(lambda c: c.data == 'clothing_ru_euro')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в евро"""
    await bot.send_message(callback_query.from_user.id, message_text_price_euro,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        euro_ru = row[5]  # Курс Евро к Русскому рублю
        await state.update_data(shipping_cost=euro_ru)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def process_price(message: types.Message, state: FSMContext):
    """Конечный расчет стоимости доставки"""
    try:
        price = float(message.text)  # Цена товара, введенная пользователем
        insurance_price = DELIVERY_RU_EUR  # Стоимость доставки в белорусских рублях
        commission_price = COMMISSION_RU_EUR  # Стоимость комиссии в белорусских рублях
        data = await state.get_data()  # Получаем данные из хранилища
        shipping_cost = data.get('shipping_cost', 0)  # Получаем стоимость доставки
        # Рассчитываем итоговую стоимость приобретения
        final_purchase_price = (price * shipping_cost) + float(insurance_price) + float(commission_price)
        rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)

        message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} руб.</b>\n"
                        "\nДля возврата в начало нажмите /start")

        await bot.send_message(message.chat.id, message_text)
        await state.finish()
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


@dp.callback_query_handler(lambda c: c.data == 'yuan_ru')
async def calculate_cost_handler(callback_query: types.CallbackQuery):
    """Насчитать стоимость доставки в зависимости от страны и типа валюты"""
    product_category_keyboard = product_category_by_russia_yuan_ru_keyboard()
    message_text_clothing = "Вы выбрали Юань.\n\nВыберите категорию товара."
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=product_category_keyboard,
                           parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == 'accessories_ru_yuan')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в Юанях"""
    await bot.send_message(callback_query.from_user.id, message_text_price_yuan, parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        yuan_ru = row[6]  # Курс Юаней к Русскому рублю
        await state.update_data(shipping_cost=yuan_ru)
        await TechStateAcceleratedByTruck.price_yuan_ru_accessories.set()  # Начальное состояние диалога с пользователем


@dp.message_handler(state=TechStateAcceleratedByTruck.price_yuan_ru_accessories)
async def process_price(message: types.Message, state: FSMContext):
    """Конечный расчет стоимости доставки"""
    try:
        price = float(message.text)  # Цена товара, введенная пользователем
        insurance_price = DELIVERY_RU_YUAN_ACCESSORIES  # Стоимость доставки в белорусских рублях
        commission_price = COMMISSION_RU_YUAN_ACCESSORIES  # Стоимость комиссии в белорусских рублях
        data = await state.get_data()  # Получаем данные из хранилища
        shipping_cost = data.get('shipping_cost', 0)  # Получаем стоимость доставки
        # Рассчитываем итоговую стоимость приобретения
        final_purchase_price = (price * shipping_cost) + float(insurance_price) + float(commission_price)
        rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)

        message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} руб.</b>\n"
                        "\nДля возврата в начало нажмите /start")

        await bot.send_message(message.chat.id, message_text)
        await state.finish()
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


@dp.callback_query_handler(lambda c: c.data == 'shoes_ru_yuan')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в Юанях"""
    await bot.send_message(callback_query.from_user.id, message_text_price_yuan, parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        yuan_ru = row[6]  # Курс Юаней к Русскому рублю
        await state.update_data(shipping_cost=yuan_ru)
        await TechStateAcceleratedByTruck.price_shoes_ru_yuan.set()  # Начальное состояние диалога с пользователем


@dp.message_handler(state=TechStateAcceleratedByTruck.price_shoes_ru_yuan)
async def process_price(message: types.Message, state: FSMContext):
    """Конечный расчет стоимости доставки"""
    try:
        price = float(message.text)  # Цена товара, введенная пользователем
        insurance_price = DELIVERY_RU_YUAN_SHOES  # Стоимость доставки в белорусских рублях
        commission_price = COMMISSION_RU_YUAN_SHOES  # Стоимость комиссии в белорусских рублях
        data = await state.get_data()  # Получаем данные из хранилища
        shipping_cost = data.get('shipping_cost', 0)  # Получаем стоимость доставки
        # Рассчитываем итоговую стоимость приобретения
        final_purchase_price = (price * shipping_cost) + float(insurance_price) + float(commission_price)
        rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)

        message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} руб.</b>\n"
                        "\nДля возврата в начало нажмите /start")

        await bot.send_message(message.chat.id, message_text)
        await state.finish()
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


@dp.callback_query_handler(lambda c: c.data == 'clothing_ru_yuan')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в Юанях"""
    await bot.send_message(callback_query.from_user.id, message_text_price_yuan, parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        yuan_ru = row[6]  # Курс Юаней к Русскому рублю
        await state.update_data(shipping_cost=yuan_ru)
        await TechStateAcceleratedByTruck.price_clothing_ru_yuan.set()  # Начальное состояние диалога с пользователем


@dp.message_handler(state=TechStateAcceleratedByTruck.price_clothing_ru_yuan)
async def process_price(message: types.Message, state: FSMContext):
    """Конечный расчет стоимости доставки"""
    try:
        price = float(message.text)  # Цена товара, введенная пользователем
        insurance_price = DELIVERY_RU_YUAN_CLOTHING  # Стоимость доставки в белорусских рублях
        commission_price = COMMISSION_RU_YUAN_CLOTHING  # Стоимость комиссии в белорусских рублях
        data = await state.get_data()  # Получаем данные из хранилища
        shipping_cost = data.get('shipping_cost', 0)  # Получаем стоимость доставки
        # Рассчитываем итоговую стоимость приобретения
        final_purchase_price = (price * shipping_cost) + float(insurance_price) + float(commission_price)
        rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)

        message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} руб.</b>\n"
                        "\nДля возврата в начало нажмите /start")

        await bot.send_message(message.chat.id, message_text)
        await state.finish()
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


def price_calculator_ru_handler():
    """Регистрируем обработчики для калькулятора"""
    dp.register_message_handler(calculate_cost_handler)  # Калькулятор цены
    dp.register_message_handler(process_delivery_handler)  # Конечный расчет стоимости доставки
