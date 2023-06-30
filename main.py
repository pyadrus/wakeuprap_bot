from aiogram import executor

from handlers.add_track_number_handlers import adding_track_number_handler
from handlers.admin_handlers import admin_handler
from handlers.application_handlers import register_application_handlers
from handlers.greeting_handlers import greeting_handler
from handlers.product_order_handlers import product_order_handler
from handlers.price_calculator_handlers import price_calculator_handler
from handlers.questions_handlers import register_answers_main_questions_handlers
from handlers.reviews_handlers import register_reviews_handler
from handlers.show_orders_handlers import my_order_handler
from handlers.user_handlers import user_handler
from system.dispatcher import dp


def main():
    executor.start_polling(dp, skip_updates=True)
    price_calculator_handler()  # Расчет стоимости
    greeting_handler()  # Начальное приветствие
    product_order_handler()  # Заказ товара пользователем
    admin_handler()  # Админ панель
    user_handler()  # Проверка статуса заказа пользователем
    register_reviews_handler()  # Отзывы пользователей
    register_answers_main_questions_handlers()  # Ответы на вопросы
    register_application_handlers()  # Приложение и сайты
    adding_track_number_handler()  # Добавление трека
    my_order_handler()  # Мои заказы


if __name__ == '__main__':
    try:
        main()  # Запуск бота
    except Exception as e:
        print(e)
