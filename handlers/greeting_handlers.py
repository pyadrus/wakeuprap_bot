import datetime
import sqlite3  # Импортируем модуль для работы с базой данных SQLite

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.admin_keyboards import admin_panel_keyboard
from keyboards.greeting_keyboards import greeting_keyboards
from messages.greeting_post import greeting_post
from system.dispatcher import dp

# Подключение к базе данных SQLite
conn = sqlite3.connect('setting/orders.db')
cursor = conn.cursor()
# Создаем таблицу, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
                                                    first_name TEXT, last_name TEXT, username TEXT, date TEXT)''')
conn.commit()


@dp.message_handler(commands=['start'])
async def greeting(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия"""
    await state.reset_state()
    # Получаем текущую дату и время
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Записываем данные пользователя в базу данных
    cursor.execute('''INSERT INTO users (user_id, first_name, last_name, username, date) VALUES (?, ?, ?, ?, ?)''',
                   (message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                    message.from_user.username, current_date))
    conn.commit()
    print(f'Привет! нажали на кнопку /start {message.from_user.id, message.from_user.username, current_date}')
    keyboards_greeting = greeting_keyboards()
    # Клавиатура для Калькулятора цен или Контактов
    await message.reply(greeting_post, reply_markup=keyboards_greeting, disable_web_page_preview=True,
                        parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands=['start_admin'])
async def greeting(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия"""
    await state.reset_state()
    # Получаем текущую дату и время
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Записываем данные пользователя в базу данных
    cursor.execute('''INSERT INTO users (user_id, first_name, last_name, username, date) VALUES (?, ?, ?, ?, ?)''',
                   (message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                    message.from_user.username, current_date))
    conn.commit()
    print(f'Привет! нажали на кнопку /start {message.from_user.id, message.from_user.username, current_date}')
    if message.from_user.id not in [5837917794, 1062323239]:  # Если это не админ, то выводим предупреждение
        await message.reply('У вас нет доступа к этой команде.')
        return
    admin_keyboard = admin_panel_keyboard()
    # Клавиатура для Калькулятора цен или Контактов
    await message.reply(greeting_post, reply_markup=admin_keyboard, disable_web_page_preview=True,
                        parse_mode=types.ParseMode.HTML)


def greeting_handler():
    """Регистрируем handlers для калькулятора"""
    dp.register_message_handler(greeting)  # Обработчик команды /start, он же пост приветствия
