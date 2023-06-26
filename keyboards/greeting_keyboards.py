from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def greeting_keyboards() -> InlineKeyboardMarkup:
    """Клавиатуры поста приветствия для всех пользователей"""
    keyboards_greeting = InlineKeyboardMarkup()
    calculate_order_amount_keyboards = InlineKeyboardButton(text='Рассчитать стоимость',
                                                            callback_data='calculate_order_amount')
    add_a_track_number_keyboards = InlineKeyboardButton(text='➕ Отследить заказ',
                                                        callback_data='add_track_number')
    keyboards_greeting.row(calculate_order_amount_keyboards, add_a_track_number_keyboards)
    make_an_order_keyboards = InlineKeyboardButton(text='🔥 Сделать заказ',
                                                   callback_data='make_an_order')
    keyboards_greeting.row(make_an_order_keyboards)
    product_selection_application = InlineKeyboardButton(text='📱 Приложения и сайты для выбора товаров',
                                                         callback_data='product_selection_application')
    keyboards_greeting.row(product_selection_application)
    answers_to_the_main_questions_keyboards = InlineKeyboardButton(text='Ответы на основные вопросы',
                                                                   callback_data='answers_to_the_main_questions')
    keyboards_greeting.row(answers_to_the_main_questions_keyboards)
    reviews_application = InlineKeyboardButton(text='🗣 Отзывы 📝',
                                               callback_data='reviews')
    keyboards_greeting.row(reviews_application)
    return keyboards_greeting


def greeting_keyboards_admin() -> InlineKeyboardMarkup:
    """Клавиатуры поста приветствия для админа"""
    keyboards_greeting_admin = InlineKeyboardMarkup()

    # Калькулятор заказов
    calculate_order_amount_keyboards = InlineKeyboardButton(text='Рассчитать стоимость',
                                                            callback_data='calculate_order_amount')

    # Пользователь добавляет трек номер и получает данные
    add_a_track_number_keyboards = InlineKeyboardButton(text='➕ Добавить трек номер',
                                                        callback_data='add_track_number')
    keyboards_greeting_admin.row(calculate_order_amount_keyboards, add_a_track_number_keyboards)

    # Получение данных о всех заказах пользователя
    my_order_keyboards = InlineKeyboardButton(text='Мои заказы',
                                              callback_data='my_order')
    keyboards_greeting_admin.row(my_order_keyboards)

    # Информационные данные для пользователя выбора товаров в приложения и сайтах
    product_selection_application = InlineKeyboardButton(text='📱 Приложения и сайты для выбора товаров',
                                                         callback_data='product_selection_application')
    keyboards_greeting_admin.row(product_selection_application)

    # Информационные данные для пользователя ответа на основные вопросы
    answers_to_the_main_questions_keyboards = InlineKeyboardButton(text='Ответы на основные вопросы',
                                                                   callback_data='answers_to_the_main_questions')
    keyboards_greeting_admin.row(answers_to_the_main_questions_keyboards)

    # Информационные данные для пользователя отзывов
    reviews_application = InlineKeyboardButton(text='🗣 Отзывы 📝',
                                               callback_data='reviews')
    keyboards_greeting_admin.row(reviews_application)

    # Админ панель для админа
    keyboards_admin = InlineKeyboardButton(text='👨‍💻 Администратор', callback_data='admin')
    keyboards_greeting_admin.row(keyboards_admin)
    return keyboards_greeting_admin


if __name__ == '__main__':
    greeting_keyboards()  # Клавиатура для пользователя
    greeting_keyboards_admin()  # Клавиатура для админа
