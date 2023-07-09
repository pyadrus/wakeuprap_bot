from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.delivery_keyboard import delivery_keyboard_technics_by, product_category_by_russia_yuan_by_keyboard
from keyboards.delivery_keyboard import product_category_by_russia_euro_by_keyboard
from keyboards.delivery_keyboard import product_category_by_russia_polish_zloty_by_keyboard
from messages.message_text_calculate import message_text_price_euro
from messages.message_text_calculate import message_text_price_polish_zloty
from messages.message_text_calculate import message_text_price_yuan
from system.dispatcher import COMMISSION_BY_YUAN_EUR
from system.dispatcher import DELIVERY_BY_EUR
from system.dispatcher import DELIVERY_BY_YUAN_ACCESSORIES
from system.dispatcher import DELIVERY_BY_YUAN_CLOTHING
from system.dispatcher import DELIVERY_BY_YUAN_SHOES
from system.dispatcher import dp, bot
from utils.database_init import get_currencies


class TechByTruck(StatesGroup):
    """Расчет стоимости доставки"""
    price_yuan_by_accessories = State()
    price_shoes_by_yuan = State()
    price_clothing_by_yuan = State()
    price_euro_by = State()


@dp.callback_query_handler(lambda c: c.data == 'belarus')
async def calculate_cost_handler(callback_query: types.CallbackQuery):
    """Насчитать стоимость доставки в зависимости от страны и типа валюты"""
    technics_delivery_keyboard = delivery_keyboard_technics_by()
    message_text_clothing = ("Вы выбрали 🇧🇾 Беларусь.\n\n"
                             "Выберите валюту.")
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=technics_delivery_keyboard,
                           parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == 'polish_zloty_by')
async def calculate_cost_handler(callback_query: types.CallbackQuery):
    """Насчитать стоимость доставки в зависимости от страны и типа валюты"""
    product_category_keyboard = product_category_by_russia_polish_zloty_by_keyboard()
    message_text_clothing = ("Вы выбрали 🇵🇱 Польский злотый.\n\n"
                             "Выберите категорию товара.")
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=product_category_keyboard,
                           parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == 'accessories_by_polish_zloty')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в польских злотых"""
    await bot.send_message(callback_query.from_user.id, message_text_price_polish_zloty,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        polish_zloty_by = row[1]  # Курс Польского злотого к Русскому рублю
        await state.update_data(shipping_cost=polish_zloty_by)
        await TechByTruck.price_euro_by.set()  # Начальное состояние диалога с пользователем


@dp.callback_query_handler(lambda c: c.data == 'shoes_by_polish_zloty')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в польских злотых"""
    await bot.send_message(callback_query.from_user.id, message_text_price_polish_zloty,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        polish_zloty_by = row[1]  # Курс Польского злотого к Русскому рублю
        await state.update_data(shipping_cost=polish_zloty_by)
        await TechByTruck.price_euro_by.set()  # Начальное состояние диалога с пользователем


@dp.callback_query_handler(lambda c: c.data == 'clothing_by_polish_zloty')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в польских злотых"""
    await bot.send_message(callback_query.from_user.id, message_text_price_polish_zloty,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        polish_zloty_by = row[1]  # Курс Польского злотого к Русскому рублю
        await state.update_data(shipping_cost=polish_zloty_by)
        await TechByTruck.price_euro_by.set()  # Начальное состояние диалога с пользователем


@dp.callback_query_handler(lambda c: c.data == 'euro_by')
async def calculate_cost_handler(callback_query: types.CallbackQuery):
    """Насчитать стоимость доставки в зависимости от страны и типа валюты"""
    product_category_keyboard = product_category_by_russia_euro_by_keyboard()
    message_text_clothing = ("Вы выбрали 🇪🇺 Евро.\n\n"
                             "Выберите категорию товара.")
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=product_category_keyboard,
                           parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == 'accessories_by_euro')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в евро"""
    await bot.send_message(callback_query.from_user.id, message_text_price_euro,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        euro_by = row[2]  # Курс Евро к Русскому рублю
        await state.update_data(shipping_cost=euro_by)
        await TechByTruck.price_euro_by.set()  # Начальное состояние диалога с пользователем


@dp.callback_query_handler(lambda c: c.data == 'shoes_by_euro')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в евро"""
    await bot.send_message(callback_query.from_user.id, message_text_price_euro,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        euro_by = row[2]  # Курс Евро к Русскому рублю
        await state.update_data(shipping_cost=euro_by)
        await TechByTruck.price_euro_by.set()  # Начальное состояние диалога с пользователем


@dp.callback_query_handler(lambda c: c.data == 'clothing_by_euro')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в евро"""
    await bot.send_message(callback_query.from_user.id, message_text_price_euro,
                           parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        euro_by = row[2]  # Курс Евро к Русскому рублю
        await state.update_data(shipping_cost=euro_by)
        await TechByTruck.price_euro_by.set()  # Начальное состояние диалога с пользователем


@dp.message_handler(state=TechByTruck.price_euro_by)
async def process_price(message: types.Message, state: FSMContext):
    """Конечный расчет стоимости доставки"""
    try:
        price = float(message.text)  # Цена товара, введенная пользователем
        data = await state.get_data()  # Получаем данные из хранилища
        shipping_cost = data.get('shipping_cost', 0)  # Получаем стоимость доставки
        # Рассчитываем итоговую стоимость приобретения
        final_purchase_price = (price * shipping_cost) + float(DELIVERY_BY_EUR) + float(COMMISSION_BY_YUAN_EUR)
        rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)

        message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} 🇧🇾 руб.</b>\n"
                        "\nДля возврата в начало нажмите /start")

        await bot.send_message(message.chat.id, message_text)
        await state.finish()
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


@dp.callback_query_handler(lambda c: c.data == 'yuan_by')
async def calculate_cost_handler(callback_query: types.CallbackQuery):
    """Насчитать стоимость доставки в зависимости от страны и типа валюты"""
    product_category_keyboard = product_category_by_russia_yuan_by_keyboard()
    message_text_clothing = ("Вы выбрали 🇨🇳 Юань.\n\n"
                             "Выберите категорию товара.")
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=product_category_keyboard,
                           parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == 'accessories_by_yuan')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в Юанях"""
    await bot.send_message(callback_query.from_user.id, message_text_price_yuan, parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        yuan_by = row[3]  # Курс Юаней к Русскому рублю
        await state.update_data(shipping_cost=yuan_by)
        await TechByTruck.price_yuan_by_accessories.set()  # Начальное состояние диалога с пользователем


@dp.message_handler(state=TechByTruck.price_yuan_by_accessories)
async def process_price(message: types.Message, state: FSMContext):
    """Конечный расчет стоимости доставки"""
    try:
        price = float(message.text)  # Цена товара, введенная пользователем
        data = await state.get_data()  # Получаем данные из хранилища
        shipping_cost = data.get('shipping_cost', 0)  # Получаем стоимость доставки
        # Рассчитываем итоговую стоимость приобретения
        final_purchase_price = (price * shipping_cost) + float(DELIVERY_BY_YUAN_ACCESSORIES) + float(COMMISSION_BY_YUAN_EUR)
        rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)

        message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} 🇧🇾 руб.</b>\n"
                        "\nДля возврата в начало нажмите /start")

        await bot.send_message(message.chat.id, message_text)
        await state.finish()
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


@dp.callback_query_handler(lambda c: c.data == 'shoes_by_yuan')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в Юанях"""
    await bot.send_message(callback_query.from_user.id, message_text_price_yuan, parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        yuan_by = row[3]  # Курс Юаней к Русскому рублю
        await state.update_data(shipping_cost=yuan_by)
        await TechByTruck.price_shoes_by_yuan.set()  # Начальное состояние диалога с пользователем


@dp.message_handler(state=TechByTruck.price_shoes_by_yuan)
async def process_price(message: types.Message, state: FSMContext):
    """Конечный расчет стоимости доставки"""
    try:
        price = float(message.text)  # Цена товара, введенная пользователем
        data = await state.get_data()  # Получаем данные из хранилища
        shipping_cost = data.get('shipping_cost', 0)  # Получаем стоимость доставки
        # Рассчитываем итоговую стоимость приобретения
        final_purchase_price = (price * shipping_cost) + float(DELIVERY_BY_YUAN_SHOES) + float(COMMISSION_BY_YUAN_EUR)
        rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)

        message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} 🇧🇾 руб.</b>\n"
                        "\nДля возврата в начало нажмите /start")

        await bot.send_message(message.chat.id, message_text)
        await state.finish()
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


@dp.callback_query_handler(lambda c: c.data == 'clothing_by_yuan')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в Юанях"""
    await bot.send_message(callback_query.from_user.id, message_text_price_yuan, parse_mode=types.ParseMode.HTML)
    row = get_currencies()
    if row:
        yuan_by = row[3]  # Курс Юаней к Русскому рублю
        await state.update_data(shipping_cost=yuan_by)
        await TechByTruck.price_clothing_by_yuan.set()  # Начальное состояние диалога с пользователем


@dp.message_handler(state=TechByTruck.price_clothing_by_yuan)
async def process_price(message: types.Message, state: FSMContext):
    """Конечный расчет стоимости доставки"""
    try:
        price = float(message.text)  # Цена товара, введенная пользователем
        data = await state.get_data()  # Получаем данные из хранилища
        shipping_cost = data.get('shipping_cost', 0)  # Получаем стоимость доставки
        # Рассчитываем итоговую стоимость приобретения
        final_purchase_price = (price * shipping_cost) + float(DELIVERY_BY_YUAN_CLOTHING) + float(COMMISSION_BY_YUAN_EUR)
        rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)

        message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} 🇧🇾 руб.</b>\n"
                        "\nДля возврата в начало нажмите /start")

        await bot.send_message(message.chat.id, message_text)
        await state.finish()
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


def price_calculator_by_handler():
    """Регистрируем обработчики для калькулятора"""
    dp.register_message_handler(calculate_cost_handler)  # Калькулятор цены
    dp.register_message_handler(process_delivery_handler)  # Конечный расчет стоимости доставки
