import logging

import requests
from aiogram import Bot, Dispatcher
from aiogram import executor
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot_token = '6059128059:AAGwrIwJ3-qXTGlH0qX1hPvUWmQvJ2jfjQY'
bot = Bot(token=bot_token, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


def get_exchange_rates():
    """Получаем курс валют от ЦБ РФ"""
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()
    return data['Valute']


def get_currency_rate(currency_code):
    rates = get_exchange_rates()
    if currency_code == 'USD':
        return rates['USD']['Value']
    elif currency_code == 'CNY':
        return rates['CNY']['Value']
    else:
        return None


usd_rate = get_currency_rate('USD')
cny_rate = get_currency_rate('CNY')

print(f'Курс доллара США: {usd_rate}')
print(f'Курс юаня: {cny_rate}')


def get_exchange_rate_usd():
    response = requests.get("https://www.cbr-xml-daily.ru/latest.js")
    data = response.json()
    return data['rates']['USD']


@dp.message_handler(Command('start'))
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    down_jacket_button = InlineKeyboardButton(text='🧥 Пуховик (пух)', callback_data='down_jacket_down')
    keyboard.row(down_jacket_button)
    await message.reply("Выберите тип товара:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'down_jacket_down')
async def down_jacket_handler(callback_query: types.CallbackQuery):
    """Обработчик расчета стоимости для пуховика"""
    keyboard = InlineKeyboardMarkup()
    scheduled_aircraft_button = InlineKeyboardButton(text='🚀 Опция "1-3 дня"', callback_data='scheduled_aircraft')
    accelerated_by_truck = InlineKeyboardButton(text='🚛 Опция "8-15 дней"', callback_data='accelerated_by_truck')
    a_regular_truck = InlineKeyboardButton(text='🚚 Опция "20-30 дней"', callback_data='a_regular_truck')
    keyboard.row(scheduled_aircraft_button)
    keyboard.row(accelerated_by_truck)
    keyboard.row(a_regular_truck)
    await bot.send_message(callback_query.from_user.id, "Выберите тип доставки:", reply_markup=keyboard)


def calculate_insurance_price(price):
    """Расчет стоимости страховки"""
    cny_rate = get_currency_rate('CNY')  # Курс Юаня к рублю
    price_in_rubles = price * cny_rate  # Переводим введенную цену пользователем в рубли
    delivery_rub_cn = 30 * cny_rate  # Цена доставки Poizon до склада в Китай
    total_price_in_rubles = delivery_rub_cn + price_in_rubles  # Цена товара
    insurance_price = (0.2 * total_price_in_rubles) / total_price_in_rubles  # Страховка
    return insurance_price  # Возвращаем цену страховки


def calculate_commission_price(price):
    """Расчет стоимости комиссии"""
    if price < 500:
        commission = 500  # Комиссия 500 рублей
    elif 500 <= price < 1000:
        commission = 750  # Комиссия 750 рублей
    elif 1000 <= price < 2000:
        commission = 1000  # Комиссия 1000 рублей
    elif price >= 2000:
        commission = price * 0.05  # 5% от стоимости заказа в рублях
    return commission


@dp.callback_query_handler(lambda c: c.data == 'scheduled_aircraft')
async def scheduled_aircraft_handler(callback_query: types.CallbackQuery):
    """Ввод пользователем цены товара в рублях"""
    await bot.send_message(callback_query.from_user.id,
                           "Введите цену товара в юанях 🇨🇳 (копейки указываются через точку):")


@dp.message_handler(content_types=types.ContentType.TEXT)
async def process_price(message: types.Message):
    try:
        cny_rate = get_currency_rate('CNY')  # Курс Юаня к рублю
        usd_rate = get_currency_rate('USD')  # Курс Доллара к рублю
        price = float(message.text)  # Цена товара в Юанях введенная пользователем
        aircraft_cost = (35 * usd_rate) * 2  # Цена доставки рейсовым самолетом 2 вес товара
        delivery_rub_cn = 30 * cny_rate  # Цена доставки Poizon до склада в Китай
        insurance_price = calculate_insurance_price(price)  # Расчет стоимости страховки
        commission_price = calculate_commission_price(price)  # Расчет стоимости комиссии
        # Рассчитываем итоговую стоимость приобретения
        final_purchase_price = (price * cny_rate) + delivery_rub_cn + insurance_price + aircraft_cost + commission_price
        rounded_number = round(final_purchase_price, 2)  # Округляем до 2х знаков
        message_text = f"<b>Общая стоимость: {rounded_number} руб.</b>\n\nДля возврата в начало нажмите /start"
        await bot.send_message(message.chat.id, message_text)
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
