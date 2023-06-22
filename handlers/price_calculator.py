# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import StatesGroup, State
#
# from keyboards.clothing_keyboard import clothing_keyboard
# from keyboards.delivery_keyboard import delivery_keyboard, delivery_keyboard_technics
# from messages.message_text_calculate import message_text_calculate, message_text_price, message_text_kg
# # from messages.message_text_clothing import message_text_clothing
# from services.exchange import get_currency_rate  # Получение курса валют
# from system.dispatcher import dp, bot
# from utils.validation import calculate_insurance_price, calculate_commission_price
#
#
# # Создаем класс состояний
# class TechStateAircraft(StatesGroup):
#     """Доставка самолетом 🚀 1-3 дня"""
#     price_Aircraft = State()
#     weight_Aircraft = State()  # Состояние для ввода веса в килограммах
#
#
# class TechStateAcceleratedByTruck(StatesGroup):
#     """Доставка ускоренной фурой 🚛 8-15 дней"""
#     price_AcceleratedByTruck = State()
#     weight_AcceleratedByTruck = State()  # Состояние для ввода веса в килограммах
#
#
# class TechStateRegularTruck(StatesGroup):
#     """Доставка обычной фурой 🚚 20-30 дней"""
#     price_RegularTruck = State()
#     weight_RegularTruck = State()  # Состояние для ввода веса в килограммах
#
#
# @dp.callback_query_handler(lambda c: c.data == 'price_calculator')
# async def calculate_cost_handler(callback_query: types.CallbackQuery):
#     """Калькулятор цены"""
#     keyboard_clothes = clothing_keyboard()
#     # Клавиатура для выбора товара
#     await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=keyboard_clothes,
#                            parse_mode=types.ParseMode.HTML)
#
#
# @dp.callback_query_handler(lambda c: c.data == 'footwear')
# async def calculate_cost_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Обработчик расчета стоимости для 👟 Обувь"""
#     delivery = delivery_keyboard()  # Клавиатура для выбора товара
#     await bot.send_message(callback_query.from_user.id, message_text_calculate, reply_markup=delivery,
#                            parse_mode=types.ParseMode.HTML)
#     exchange_rate = 1  # Масса в 1 кг
#     await state.update_data(exchange_rate=exchange_rate)  # Функция для обновления данных в состоянии, аналог return
#
#
# @dp.callback_query_handler(lambda c: c.data == 'trousers')
# async def calculate_cost_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Обработчик расчета стоимости для 👖 Штаны"""
#     delivery = delivery_keyboard()  # Клавиатура для выбора товара
#     await bot.send_message(callback_query.from_user.id, message_text_calculate, reply_markup=delivery,
#                            parse_mode=types.ParseMode.HTML)
#     exchange_rate = 0.8  # Масса в 0.8 кг
#     await state.update_data(exchange_rate=exchange_rate)  # Функция для обновления данных в состоянии, аналог return
#
#
# @dp.callback_query_handler(lambda c: c.data == 'hoodies')
# async def calculate_cost_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Обработчик расчета стоимости для 🥼 Худи"""
#     delivery = delivery_keyboard()  # Клавиатура для выбора товара
#     await bot.send_message(callback_query.from_user.id, message_text_calculate, reply_markup=delivery,
#                            parse_mode=types.ParseMode.HTML)
#     exchange_rate = 1  # Масса в 1 кг
#     await state.update_data(exchange_rate=exchange_rate)  # Функция для обновления данных в состоянии, аналог return
#
#
# @dp.callback_query_handler(lambda c: c.data == 'down_jacket_down')
# async def calculate_cost_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Обработчик расчета стоимости для 🧥 Пуховик (пух)"""
#     delivery = delivery_keyboard()  # Клавиатура для выбора товара
#     await bot.send_message(callback_query.from_user.id, message_text_calculate, reply_markup=delivery,
#                            parse_mode=types.ParseMode.HTML)
#     exchange_rate = 2  # Масса в 2 кг
#     await state.update_data(exchange_rate=exchange_rate)  # Функция для обновления данных в состоянии, аналог return
#
#
# @dp.callback_query_handler(lambda c: c.data == 'down_jacket_synthetic')
# async def calculate_cost_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Обработчик расчета стоимости для 🧥 Пуховик (синтетика)"""
#     delivery = delivery_keyboard()  # Клавиатура для выбора товара
#     await bot.send_message(callback_query.from_user.id, message_text_calculate, reply_markup=delivery,
#                            parse_mode=types.ParseMode.HTML)
#     exchange_rate = 1.2  # Масса в 1.2 кг
#     await state.update_data(exchange_rate=exchange_rate)  # Функция для обновления данных в состоянии, аналог return
#
#
# @dp.callback_query_handler(lambda c: c.data == 'backpack')
# async def calculate_cost_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Обработчик расчета стоимости для 🎒 Рюкзак"""
#     delivery = delivery_keyboard()  # Клавиатура для выбора товара
#     await bot.send_message(callback_query.from_user.id, message_text_calculate, reply_markup=delivery,
#                            parse_mode=types.ParseMode.HTML)
#     exchange_rate = 0.6  # Масса в 0.6 кг
#     await state.update_data(exchange_rate=exchange_rate)  # Функция для обновления данных в состоянии, аналог return
#
#
# @dp.callback_query_handler(lambda c: c.data == 'shoulder_bag')
# async def calculate_cost_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Обработчик расчета стоимости для 👜 Сумка наплечная"""
#     delivery = delivery_keyboard()  # Клавиатура для выбора товара
#     await bot.send_message(callback_query.from_user.id, message_text_calculate, reply_markup=delivery,
#                            parse_mode=types.ParseMode.HTML)
#     exchange_rate = 0.2  # Масса в 0.2 кг
#     await state.update_data(exchange_rate=exchange_rate)  # Функция для обновления данных в состоянии, аналог return
#
#
# @dp.callback_query_handler(lambda c: c.data == 'longsleeve')
# async def calculate_cost_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Обработчик расчета стоимости для 👕 Лонгслив / майка"""
#     delivery = delivery_keyboard()  # Клавиатура для выбора товара
#     await bot.send_message(callback_query.from_user.id, message_text_calculate, reply_markup=delivery,
#                            parse_mode=types.ParseMode.HTML)
#     exchange_rate = 0.4  # Масса в 0.4 кг
#     await state.update_data(exchange_rate=exchange_rate)  # Функция для обновления данных в состоянии, аналог return
#
#
# """Виды доставки"""
#
#
# @dp.callback_query_handler(lambda c: c.data == 'scheduled_aircraft')
# async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Ввод пользователем цены товара в рублях 🚀 Опция "1-3 дня"""
#     await bot.send_message(callback_query.from_user.id, message_text_price, parse_mode=types.ParseMode.HTML)
#     usd_rate = get_currency_rate('USD')  # Курс Доллара к рублю
#     data = await state.get_data()
#     exchange_rate = data.get('exchange_rate', 0)  # Вес товара
#     shipping_cost = (35 * usd_rate) * exchange_rate
#     # Функция для обновления данных в состоянии, аналог return
#     await state.update_data(shipping_cost=shipping_cost)
#
#
# @dp.callback_query_handler(lambda c: c.data == 'accelerated_by_truck')
# async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Ввод пользователем цены товара в рублях 🚛 Опция "8-15 дней"""
#     await bot.send_message(callback_query.from_user.id, message_text_price, parse_mode=types.ParseMode.HTML)
#     usd_rate = get_currency_rate('USD')  # Курс Доллара к рублю
#     data = await state.get_data()
#     exchange_rate = data.get('exchange_rate', 0)  # Вес товара
#     shipping_cost = (12 * usd_rate) * exchange_rate
#     # Функция для обновления данных в состоянии, аналог return
#     await state.update_data(shipping_cost=shipping_cost)
#
#
# @dp.callback_query_handler(lambda c: c.data == 'a_regular_truck')
# async def process_delivery_handler(callback_query: types.CallbackQuery, state: FSMContext):
#     """Ввод пользователем цены товара в рублях 🚚 Опция "20-30 дней"""
#     await bot.send_message(callback_query.from_user.id, message_text_price, parse_mode=types.ParseMode.HTML)
#     usd_rate = get_currency_rate('USD')  # Курс Доллара к рублю
#     data = await state.get_data()
#     exchange_rate = data.get('exchange_rate', 0)  # Вес товара
#     shipping_cost = (6 * usd_rate) * exchange_rate
#     # Функция для обновления данных в состоянии, аналог return
#     await state.update_data(shipping_cost=shipping_cost)
#
#
# @dp.message_handler(content_types=types.ContentType.TEXT)
# async def process_price(message: types.Message, state: FSMContext):
#     """
#     Конечный расчет стоимости доставки: Цена товара + Доставка Poizon до склада в Китае + Страховка +
#                                         Доставка из Китая в Москву + Комиссия = Конечная стоимость товара.
#     """
#     try:
#         cny_rate = get_currency_rate('CNY')  # Курс Юаня к рублю
#         price = float(message.text)  # Цена товара в Юанях введенная пользователем
#         delivery_rub_cn = 30 * cny_rate  # Цена доставки Poizon до склада в Китай
#         insurance_price = calculate_insurance_price(price)  # Расчет стоимости страховки
#         commission_price = calculate_commission_price(price)  # Расчет стоимости комиссии
#         data = await state.get_data()
#         shipping_cost = data.get('shipping_cost', 0)  # Максимальная стоимость доставки из Китая в Москву
#         # Рассчитываем итоговые стоимости приобретения
#         final_purchase_price = (price * cny_rate) + delivery_rub_cn + insurance_price + shipping_cost + commission_price
#         rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)
#
#         message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} руб.</b>\n"
#                         "\nДля возврата в начало нажмите /start")
#
#         await bot.send_message(message.chat.id, message_text)
#         await state.finish()
#     except ValueError:
#         await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")
#
#
# # Обработчик выбора типа техники
# @dp.callback_query_handler(lambda c: c.data == 'technics')
# async def process_technics(callback_query: types.CallbackQuery):
#     """Обработчик выбора типа техники"""
#     technics_delivery_keyboard = delivery_keyboard_technics()
#     await bot.send_message(callback_query.from_user.id, message_text_calculate, reply_markup=technics_delivery_keyboard)
#
#
# @dp.callback_query_handler(lambda c: c.data == "technics_a_regular_truck")
# async def process_delivery_handler(query: types.CallbackQuery):
#     """Ввод пользователем цены товара в рублях 🚚 20-30 дней"""
#     await bot.send_message(query.from_user.id, message_text_kg, parse_mode=types.ParseMode.HTML)
#     await TechStateRegularTruck.weight_RegularTruck.set()  # Переходим в состояние ожидания веса в килограммах
#
#
# @dp.callback_query_handler(lambda c: c.data == "technics_accelerated_by_truck")
# async def process_delivery_handler(query: types.CallbackQuery):
#     """Ввод пользователем цены товара в рублях 🚛 8-15 дней"""
#     await bot.send_message(query.from_user.id, message_text_kg, parse_mode=types.ParseMode.HTML)
#     await TechStateAcceleratedByTruck.weight_AcceleratedByTruck.set()  # Переходим в состояние ожидания веса в кг.
#
#
# @dp.callback_query_handler(lambda c: c.data == "technics_aircraft")
# async def process_delivery_handler(query: types.CallbackQuery):
#     """Ввод пользователем цены товара в рублях 🚀 1-3 дня"""
#     await bot.send_message(query.from_user.id, message_text_kg, parse_mode=types.ParseMode.HTML)
#     await TechStateAircraft.weight_Aircraft.set()  # Переходим в состояние ожидания веса в килограммах
#
#
# @dp.message_handler(state=TechStateAcceleratedByTruck.weight_AcceleratedByTruck)
# async def process_weight(message: types.Message, state: FSMContext):
#     """Обработка введенного веса техники 🚛 8-15 дней"""
#     exchange_rate = float(message.text)  # Вес товара
#     usd_rate = get_currency_rate('USD')  # Курс Доллара к рублю
#     shipping_cost = (12 * usd_rate) * exchange_rate
#     await state.update_data(shipping_cost=shipping_cost)
#     await TechStateAcceleratedByTruck.price_AcceleratedByTruck.set()  # Переходим в состояние ожидания ввода цены
#     await bot.send_message(message.from_user.id, message_text_price, parse_mode=types.ParseMode.HTML)
#
#
# @dp.message_handler(state=TechStateRegularTruck.weight_RegularTruck)
# async def process_weight(message: types.Message, state: FSMContext):
#     """Обработка введенного веса техники 🚚 20-30 дней"""
#     exchange_rate = float(message.text)  # Вес товара
#     usd_rate = get_currency_rate('USD')  # Курс Доллара к рублю
#     shipping_cost = (6 * usd_rate) * exchange_rate
#     await state.update_data(shipping_cost=shipping_cost)
#     await TechStateRegularTruck.price_RegularTruck.set()  # Переходим в состояние ожидания ввода цены
#     await bot.send_message(message.from_user.id, message_text_price, parse_mode=types.ParseMode.HTML)
#
#
# @dp.message_handler(state=TechStateAircraft.weight_Aircraft)
# async def process_weight(message: types.Message, state: FSMContext):
#     """Обработка введенного веса техники 🚀 1-3 дня"""
#     exchange_rate = float(message.text)  # Вес товара
#     usd_rate = get_currency_rate('USD')  # Курс Доллара к рублю
#     shipping_cost = (35 * usd_rate) * exchange_rate
#     await state.update_data(shipping_cost=shipping_cost)
#     await TechStateAircraft.price_Aircraft.set()  # Переходим в состояние ожидания ввода цены
#     await bot.send_message(message.from_user.id, message_text_price, parse_mode=types.ParseMode.HTML)
#
#
# @dp.message_handler(state=TechStateAircraft.price_Aircraft)
# async def process_price_input(message: types.Message, state: FSMContext):
#     """Обработка введенной цены товара 🚀 1-3 дня"""
#     try:
#         await process_price_aircraft(message, state)  # Вызов калькулятора стоимости после получения цены
#     except ValueError:
#         await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение для цены товара.")
#
#
# @dp.message_handler(state=TechStateAcceleratedByTruck.price_AcceleratedByTruck)
# async def process_price_input(message: types.Message, state: FSMContext):
#     """Обработка введенной цены товара 🚛 8-15 дней"""
#     try:
#         await process_price_accelerated_by_truck(message, state)  # Вызов калькулятора стоимости после получения цены
#     except ValueError:
#         await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение для цены товара.")
#
#
# @dp.message_handler(state=TechStateRegularTruck.price_RegularTruck)
# async def process_price_input(message: types.Message, state: FSMContext):
#     """Обработка введенной цены товара 🚚 20-30 дней"""
#     try:
#         await process_price_regular_truck(message, state)  # Вызов калькулятора стоимости после получения цены
#     except ValueError:
#         await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение для цены товара.")
#
#
# async def process_price_aircraft(message: types.Message, state: FSMContext):
#     """
#     Конечный расчет стоимости доставки: Цена товара + Доставка Poizon до склада в Китае + Страховка +
#                                         Доставка из Китая в Москву + Комиссия = Конечная стоимость товара.
#     """
#     try:
#         # Получение уникальных параметров для типа техники "Доставка самолетом"
#         data = await state.get_data()
#         shipping_cost = data.get('shipping_cost', 0)  # Максимальная стоимость доставки из Китая в Москву
#         cny_rate = get_currency_rate('CNY')  # Курс Юаня к рублю
#         price = float(message.text)  # Цена товара в Юанях введенная пользователем
#         delivery_rub_cn = 30 * cny_rate  # Цена доставки Poizon до склада в Китай
#         insurance_price = calculate_insurance_price(price)  # Расчет стоимости страховки
#         commission_price = calculate_commission_price(price)  # Расчет стоимости комиссии
#         # Рассчитываем итоговые стоимости приобретения
#         final_purchase_price = (price * cny_rate) + delivery_rub_cn + insurance_price + shipping_cost + commission_price
#         rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)
#         message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} руб.</b>\n"
#                         "\nДля возврата в начало нажмите /start")
#         await bot.send_message(message.chat.id, message_text)
#         await state.finish()
#     except ValueError:
#         await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")
#
#
# async def process_price_accelerated_by_truck(message: types.Message, state: FSMContext):
#     """
#     Конечный расчет стоимости доставки: Цена товара + Доставка Poizon до склада в Китае + Страховка +
#                                         Доставка из Китая в Москву + Комиссия = Конечная стоимость товара.
#     """
#     try:
#         data = await state.get_data()
#         shipping_cost = data.get('shipping_cost', 0)  # Максимальная стоимость доставки из Китая в Москву
#         cny_rate = get_currency_rate('CNY')  # Курс Юаня к рублю
#         price = float(message.text)  # Цена товара в Юанях введенная пользователем
#         delivery_rub_cn = 30 * cny_rate  # Цена доставки Poizon до склада в Китай
#         insurance_price = calculate_insurance_price(price)  # Расчет стоимости страховки
#         commission_price = calculate_commission_price(price)  # Расчет стоимости комиссии
#         # Рассчитываем итоговые стоимости приобретения
#         final_purchase_price = (price * cny_rate) + delivery_rub_cn + insurance_price + shipping_cost + commission_price
#         rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)
#         message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} руб.</b>\n"
#                         "\nДля возврата в начало нажмите /start")
#         await bot.send_message(message.chat.id, message_text)
#         await state.finish()
#     except ValueError:
#         await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")
#
#
# async def process_price_regular_truck(message: types.Message, state: FSMContext):
#     """
#     Конечный расчет стоимости доставки: Цена товара + Доставка Poizon до склада в Китае + Страховка +
#                                         Доставка из Китая в Москву + Комиссия = Конечная стоимость товара.
#     """
#     try:
#         data = await state.get_data()
#         shipping_cost = data.get('shipping_cost', 0)  # Максимальная стоимость доставки из Китая в Москву
#         cny_rate = get_currency_rate('CNY')  # Курс Юаня к рублю
#         price = float(message.text)  # Цена товара в Юанях введенная пользователем
#         delivery_rub_cn = 30 * cny_rate  # Цена доставки Poizon до склада в Китай
#         insurance_price = calculate_insurance_price(price)  # Расчет стоимости страховки
#         commission_price = calculate_commission_price(price)  # Расчет стоимости комиссии
#         # Рассчитываем итоговые стоимости приобретения
#         final_purchase_price = (price * cny_rate) + delivery_rub_cn + insurance_price + shipping_cost + commission_price
#         rounded_number = round(final_purchase_price, 2)  # Округляем до 2 знаков (максимальная стоимость)
#         message_text = (f"<b>Общая стоимость заказа ≈ {rounded_number} руб.</b>\n"
#                         "\nДля возврата в начало нажмите /start")
#         await bot.send_message(message.chat.id, message_text)
#         await state.finish()
#     except ValueError:
#         await bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")
#
#
# def price_calculator_handler():
#     """Регистрируем handlers для калькулятора"""
#     dp.register_message_handler(calculate_cost_handler)  # Калькулятор цены
#     dp.register_message_handler(process_delivery_handler)  # Ввод пользователем цены товара в рублях 🚀 Опция "1-3 дня
#     dp.register_message_handler(process_price)  # Конечный расчет стоимости доставки
#     dp.register_message_handler(process_technics)  # Обработчик выбора типа техники
#     dp.register_message_handler(process_delivery_handler)  # Ввод пользователем цены товара в рублях 🚀 Опция "1-3 дня
#     dp.register_message_handler(process_weight)  # Обработка введенного веса техники 🚛 8-15 дней
#     dp.register_message_handler(process_price_input)  # Обработка введенной цены товара 🚀 1-3 дня
#     dp.register_message_handler(process_price_regular_truck)  # Конечный расчет стоимости доставки
#     dp.register_message_handler(process_price_accelerated_by_truck)  # Конечный расчет стоимости доставки
#     dp.register_message_handler(process_price_aircraft)  # Конечный расчет стоимости доставки
