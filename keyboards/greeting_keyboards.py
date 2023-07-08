from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def greeting_keyboards() -> InlineKeyboardMarkup:
    """Клавиатуры поста приветствия для всех пользователей"""
    keyboards_greeting = InlineKeyboardMarkup()
    add_track_number = InlineKeyboardButton(text='➕ Добавить трек номер', callback_data='add_track_number')
    # Получение данных о всех заказах пользователя
    my_order_keyboards = InlineKeyboardButton(text='📦 Мои заказы', callback_data='my_order')
    keyboards_greeting.row(add_track_number, my_order_keyboards)
    make_an_order_keyboards = InlineKeyboardButton(text='🔥 Оформить заказ 🔥 ', callback_data='make_an_order_user')
    keyboards_greeting.row(make_an_order_keyboards)
    calculate_order = InlineKeyboardButton(text='💵 Рассчитать стоимость', callback_data='calculate_order_amount')
    keyboards_greeting.row(calculate_order)
    # Информационные данные для пользователя выбора товаров в приложения и сайтах
    product_selection_application = InlineKeyboardButton(text='📱 Приложения и сайты для выбора товаров',
                                                         callback_data='product_selection_application')
    keyboards_greeting.row(product_selection_application)
    # Информационные данные для пользователя ответа на основные вопросы
    answers_main_questions = InlineKeyboardButton(text='✏️ Ответы на основные вопросы',
                                                  callback_data='answers_main_questions')
    keyboards_greeting.row(answers_main_questions)
    # Информационные данные для пользователя отзывов
    reviews_application = InlineKeyboardButton(text='🔉 Отзывы', callback_data='reviews')
    keyboards_greeting.row(reviews_application)
    return keyboards_greeting


if __name__ == '__main__':
    greeting_keyboards()  # Клавиатура для пользователя
