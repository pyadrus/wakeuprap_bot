import configparser
import logging

from aiogram import Bot, Dispatcher
from aiogram import executor
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.inline_keyboards import clothing_keyboard, delivery_keyboard
from services.exchange import get_currency_rate

config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)
config.read("setting/config.ini")
bot_token = config.get('BOT_TOKEN', 'BOT_TOKEN')

bot = Bot(token=bot_token, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(Command('start'))
async def start_handler(message: types.Message):
    keyboard_clothes = clothing_keyboard()
    await message.reply("Выберите тип товара:", reply_markup=keyboard_clothes)


@dp.callback_query_handler(lambda c: c.data == 'down_jacket_down')
async def down_jacket_handler(callback_query: types.CallbackQuery):
    """Обработчик расчета стоимости для пуховика"""
    delivery = delivery_keyboard()
    await bot.send_message(callback_query.from_user.id, "Выберите тип доставки:", reply_markup=delivery)


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
async def process_price(message: types.Message, state: FSMContext):
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
        await state.finish()
    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
