from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.delivery_keyboard import delivery_keyboard_technics
from messages.message_text_calculate import message_text_price_polish_zloty, message_text_price_euro, \
    message_text_price_yuan
from system.dispatcher import dp, bot, DELIVERY_BELARUS, COMMISSION_BELARUS


class TechStateAcceleratedByTruck(StatesGroup):
    """Расчет стоимости доставки"""
    price_AcceleratedByTruck = State()
    weight_AcceleratedByTruck = State()  # Состояние для ввода веса в килограммах


@dp.callback_query_handler(lambda c: c.data == 'calculate_order_amount')
async def calculate_cost_handler(callback_query: types.CallbackQuery):
    """Калькулятор цены исходя из типа валюты"""
    message_text_clothing = "Выберите тип валюты для расчета:"
    technics_delivery_keyboard = delivery_keyboard_technics()
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=technics_delivery_keyboard,
                           parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == 'polish_zloty')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в польских злотых"""
    await bot.send_message(callback_query.from_user.id, message_text_price_polish_zloty, parse_mode=types.ParseMode.HTML)
    usd_rate = 0.75  # Курс Польского злотого к белорусскому рублю
    await state.update_data(shipping_cost=usd_rate)


@dp.callback_query_handler(lambda c: c.data == 'euro')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в евро"""
    await bot.send_message(callback_query.from_user.id, message_text_price_euro, parse_mode=types.ParseMode.HTML)
    usd_rate = 3.34  # Курс Евро к Белорусскому рублю
    await state.update_data(shipping_cost=usd_rate)


@dp.callback_query_handler(lambda c: c.data == 'yuan')
async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
    """Подсчет стоимости доставки товара в Юанях"""
    await bot.send_message(callback_query.from_user.id, message_text_price_yuan, parse_mode=types.ParseMode.HTML)
    usd_rate = 0.48  # Курс Юаней к Белорусскому рублю
    await state.update_data(shipping_cost=usd_rate)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def process_price(message: types.Message, state: FSMContext):
    """Конечный расчет стоимости доставки"""
    try:
        price = float(message.text)  # Цена товара, введенная пользователем
        insurance_price = DELIVERY_BELARUS  # Стоимость доставки в белорусских рублях
        commission_price = COMMISSION_BELARUS  # Стоимость комиссии в белорусских рублях
        data = await state.get_data()  # Получаем данные из хранилища
        shipping_cost = data.get('shipping_cost', 0)  # Получаем стоимость доставки
        # Рассчитываем итоговую стоимость приобретения
        final_purchase_price = (price * shipping_cost) + insurance_price + commission_price
        rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)

        message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} руб.</b>\n"
                        "\nДля возврата в начало нажмите /start")

        await bot.send_message(message.chat.id, message_text)
        await state.finish()
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


def price_calculator_handler():
    """Регистрируем обработчики для калькулятора"""
    dp.register_message_handler(calculate_cost_handler)  # Калькулятор цены
    dp.register_message_handler(process_price)  # Конечный расчет стоимости доставки
