import sqlite3


def connecting_database():
    """Подключение к базе данных SQLite"""
    with sqlite3.connect("setting/orders.db") as conn:  # Подключение к базе данных SQLite
        cursor = conn.cursor()
        return conn, cursor


def creating_table_for_orders():
    """Создание таблицы для заказов"""
    with sqlite3.connect("setting/orders.db") as conn:  # Подключение к базе данных SQLite
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS orders (user_id, name, phone, link, size, color, price, order_number, date)""")
        conn.commit()


def creating_table_for_monitoring_user():
    """Создание таблицы для мониторинга пользователя"""
    with sqlite3.connect("setting/orders.db") as conn:  # Подключение к базе данных SQLite
        cursor = conn.cursor()
        # Создаем таблицу, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,
                                                        first_name TEXT, last_name TEXT, username TEXT, date TEXT)''')
        conn.commit()


if __name__ == '__main__':
    creating_table_for_orders()
    creating_table_for_monitoring_user()
