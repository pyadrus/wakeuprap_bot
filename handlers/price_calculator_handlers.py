from aiogram import types

from keyboards.delivery_keyboard import country_delivery_keyboard
from system.dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == 'calculate_order_amount')
async def calculate_cost_handler(callback_query: types.CallbackQuery):
    """Насчитать стоимость доставки в зависимости от страны и типа валюты"""
    message_text_clothing = "Выберите страну проживания.\n\nВ зависимости от страны, будет показана стоимость доставки."
    delivery_keyboard = country_delivery_keyboard()
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=delivery_keyboard,
                           parse_mode=types.ParseMode.HTML)


def price_calculator_handler():
    """Регистрируем обработчики для калькулятора"""
    dp.register_message_handler(calculate_cost_handler)  # Калькулятор цены
