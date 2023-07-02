import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.admin_keyboards import currency_exchange_rate_keyboard
from system.dispatcher import dp, bot


class ExchangeRate(StatesGroup):
    """Статусы заказа"""
    byn_pln = State()
    byn_eur = State()
    byn_yuan = State()
    rub_pln = State()
    rub_eur = State()
    rub_yuan = State()


@dp.callback_query_handler(lambda c: c.data == 'change_exchange_rate')
async def exchange_rate_handlers(callback_query: types.CallbackQuery):
    """Приложение и сайты"""
    message_text_clothing = "Выберите валютную пару для изменения курса валют"
    # Клавиатура для изменения курса валют
    cur_exchange_rate_keyboard = currency_exchange_rate_keyboard()
    await bot.send_message(callback_query.from_user.id, message_text_clothing, reply_markup=cur_exchange_rate_keyboard,
                           disable_web_page_preview=True,
                           parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(lambda c: c.data == 'byn_pln_button')
async def byn_pln_handlers(callback_query: types.CallbackQuery):
    """Ввод курса валюты белорусский рубль к польскому злотому"""
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Введите курс валюты")
    # Переходим в состояние ожидания ввода курса валюты BYN/PLN
    await ExchangeRate.byn_pln.set()


@dp.callback_query_handler(lambda c: c.data == 'byn_eur_button')
async def byn_eur_handlers(callback_query: types.CallbackQuery):
    """Ввод курса валюты белорусский рубль к евро"""
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Введите курс валюты")
    # Переходим в состояние ожидания ввода курса валюты BYN/EUR
    await ExchangeRate.byn_eur.set()


@dp.callback_query_handler(lambda c: c.data == 'byn_yuan_button')
async def byn_yuan_handlers(callback_query: types.CallbackQuery):
    """Ввод курса валюты белорусский рубль к юаню"""
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Введите курс валюты")
    # Переходим в состояние ожидания ввода курса валюты BYN/YUAN
    await ExchangeRate.byn_yuan.set()


@dp.callback_query_handler(lambda c: c.data == 'rub_pln_button')
async def rub_pln_handlers(callback_query: types.CallbackQuery):
    """Ввод курса валюты российский рубль к польскому злотому"""
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Введите курс валюты")
    # Переходим в состояние ожидания ввода курса валюты RUB/PLN
    await ExchangeRate.rub_pln.set()


@dp.callback_query_handler(lambda c: c.data == 'rub_eur_button')
async def rub_eur_handlers(callback_query: types.CallbackQuery):
    """Ввод курса валюты российский рубль к евро"""
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Введите курс валюты")
    # Переходим в состояние ожидания ввода курса валюты RUB/EUR
    await ExchangeRate.rub_eur.set()


@dp.callback_query_handler(lambda c: c.data == 'rub_yuan_button')
async def rub_yuan_handlers(callback_query: types.CallbackQuery):
    """Ввод курса валюты российский рубль к юаню"""
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Введите курс валюты")
    # Переходим в состояние ожидания ввода курса валюты RUB/YUAN
    await ExchangeRate.rub_yuan.set()


# Подключение к базе данных SQLite
conn = sqlite3.connect('setting/orders.db')
cursor = conn.cursor()
# Создаем таблицу currencies, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS currencies 
                  (id INTEGER PRIMARY KEY, BYN_PLN REAL, BYN_EUR REAL, BYN_YUAN REAL, RUB_PLN REAL, RUB_EUR REAL, RUB_YUAN REAL)''')
conn.commit()


@dp.message_handler(state=ExchangeRate.byn_pln)
async def byn_pln_handlers(message: types.Message, state: FSMContext):
    byn_pln = float(message.text)
    currency = 'BYN_PLN'
    rate = byn_pln
    cursor.execute("SELECT * FROM currencies")
    existing_record = cursor.fetchone()
    if existing_record:
        # Если запись существует, обновляем значения в ней
        cursor.execute("UPDATE currencies SET BYN_PLN=? WHERE id=?", (rate, 1))
        conn.commit()
        await message.reply(
            f"🌍 Курс {currency} успешно обновлен! 🌍 \n\n📌 Для возврата в начальное меню, нажмите /start_admin 📌 ")
    else:
        # Если запись не существует, вставляем новую запись
        cursor.execute("INSERT INTO currencies (id, BYN_PLN) VALUES (?, ?)", (1, rate))
        conn.commit()
        await message.reply(f"Курс {currency} успешно добавлен!")
    await state.finish()


@dp.message_handler(state=ExchangeRate.byn_eur)
async def byn_eur_handlers(message: types.Message, state: FSMContext):
    byn_eur = float(message.text)
    currency = 'BYN_EUR'
    rate = byn_eur
    cursor.execute("SELECT * FROM currencies")
    existing_record = cursor.fetchone()
    if existing_record:
        # Если запись существует, обновляем курс валюты
        cursor.execute("UPDATE currencies SET BYN_EUR=? WHERE id=?", (rate, 1))
        conn.commit()
        await message.reply(
            f"🌍 Курс {currency} успешно обновлен! 🌍 \n\n📌 Для возврата в начальное меню, нажмите /start_admin 📌 ")
    else:
        # Если запись не существует, вставляем новую запись
        cursor.execute("INSERT INTO currencies (id, BYN_EUR) VALUES (?, ?)", (1, rate))
        conn.commit()
        await message.reply(f"Курс {currency} успешно добавлен!")
    await state.finish()


@dp.message_handler(state=ExchangeRate.byn_yuan)
async def byn_yuan_handlers(message: types.Message, state: FSMContext):
    byn_yuan = float(message.text)
    currency = 'BYN_YUAN'
    rate = byn_yuan
    cursor.execute("SELECT * FROM currencies")
    existing_record = cursor.fetchone()
    if existing_record:
        # Если запись существует, обновляем курс валюты
        cursor.execute("UPDATE currencies SET BYN_YUAN=? WHERE id=?", (rate, 1))
        conn.commit()
        await message.reply(
            f"🌍 Курс {currency} успешно обновлен! 🌍 \n\n📌 Для возврата в начальное меню, нажмите /start_admin 📌 ")
    else:
        # Если запись не существует, вставляем новую запись
        cursor.execute("INSERT INTO currencies (id, BYN_YUAN) VALUES (?, ?)", (1, rate))
        conn.commit()
        await message.reply(f"Курс {currency} успешно добавлен!")
    await state.finish()


@dp.message_handler(state=ExchangeRate.rub_pln)
async def rub_pln_handlers(message: types.Message, state: FSMContext):
    rub_pln = float(message.text)
    currency = 'RUB_PLN'
    rate = rub_pln
    cursor.execute("SELECT * FROM currencies")
    existing_record = cursor.fetchone()
    if existing_record:
        # Если запись существует, обновляем курс валюты
        cursor.execute("UPDATE currencies SET RUB_PLN=? WHERE id=?", (rate, 1))
        conn.commit()
        await message.reply(
            f"🌍 Курс {currency} успешно обновлен! 🌍 \n\n📌 Для возврата в начальное меню, нажмите /start_admin 📌 ")
    else:
        # Если запись не существует, вставляем новую запись
        cursor.execute("INSERT INTO currencies (id, RUB_PLN) VALUES (?, ?)", (1, rate))
        conn.commit()
        await message.reply(f"Курс {currency} успешно добавлен!")
    await state.finish()


@dp.message_handler(state=ExchangeRate.rub_eur)
async def rub_eur_handlers(message: types.Message, state: FSMContext):
    rub_eur = float(message.text)
    currency = 'RUB_EUR'
    rate = rub_eur
    cursor.execute("SELECT * FROM currencies")
    existing_record = cursor.fetchone()
    if existing_record:
        # Если запись существует, обновляем курс валюты
        cursor.execute("UPDATE currencies SET RUB_EUR=? WHERE id=?", (rate, 1))
        conn.commit()
        await message.reply(
            f"🌍 Курс {currency} успешно обновлен! 🌍 \n\n📌 Для возврата в начальное меню, нажмите /start_admin 📌 ")
    else:
        # Если запись не существует, вставляем новую запись
        cursor.execute("INSERT INTO currencies (id, RUB_EUR) VALUES (?, ?)", (1, rate))
        conn.commit()
        await message.reply(f"Курс {currency} успешно добавлен!")
    await state.finish()


@dp.message_handler(state=ExchangeRate.rub_yuan)
async def rub_yuan_handlers(message: types.Message, state: FSMContext):
    rub_yuan = float(message.text)
    currency = 'RUB_YUAN'
    rate = rub_yuan
    cursor.execute("SELECT * FROM currencies")
    existing_record = cursor.fetchone()
    if existing_record:
        # Если запись существует, обновляем курс валюты
        cursor.execute("UPDATE currencies SET RUB_YUAN=? WHERE id=?", (rate, 1))
        conn.commit()
        await message.reply(
            f"🌍 Курс {currency} успешно обновлен! 🌍 \n\n📌 Для возврата в начальное меню, нажмите /start_admin 📌 ")
    else:
        # Если запись не существует, вставляем новую запись
        cursor.execute("INSERT INTO currencies (id, RUB_YUAN) VALUES (?, ?)", (1, rate))
        conn.commit()
        await message.reply(f"Курс {currency} успешно добавлен!")
    await state.finish()


def register_exchange_rate_handlers():
    """Регистрируем handlers для обработчиков сообщений"""
    dp.register_message_handler(exchange_rate_handlers)
    dp.register_message_handler(byn_pln_handlers)
    dp.register_message_handler(byn_eur_handlers)
    dp.register_message_handler(byn_yuan_handlers)
    dp.register_message_handler(rub_pln_handlers)
    dp.register_message_handler(rub_eur_handlers)
    dp.register_message_handler(rub_yuan_handlers)
