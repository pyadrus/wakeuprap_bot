from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def greeting_keyboards():
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


def greeting_keyboards_admin():
    """Клавиатуры поста приветствия для админа"""
    keyboards_greeting_admin = InlineKeyboardMarkup()
    calculate_order_amount_keyboards = InlineKeyboardButton(text='Рассчитать стоимость',
                                                            callback_data='calculate_order_amount')
    add_a_track_number_keyboards = InlineKeyboardButton(text='➕ Отследить заказ',
                                                        callback_data='add_track_number')
    keyboards_greeting_admin.row(calculate_order_amount_keyboards, add_a_track_number_keyboards)
    make_an_order_keyboards = InlineKeyboardButton(text='🔥 Сделать заказ',
                                                   callback_data='make_an_order')
    keyboards_greeting_admin.row(make_an_order_keyboards)
    product_selection_application = InlineKeyboardButton(text='📱 Приложения и сайты для выбора товаров',
                                                         callback_data='product_selection_application')
    keyboards_greeting_admin.row(product_selection_application)
    answers_to_the_main_questions_keyboards = InlineKeyboardButton(text='Ответы на основные вопросы',
                                                                   callback_data='answers_to_the_main_questions')
    keyboards_greeting_admin.row(answers_to_the_main_questions_keyboards)
    reviews_application = InlineKeyboardButton(text='🗣 Отзывы 📝',
                                               callback_data='reviews')
    keyboards_greeting_admin.row(reviews_application)
    keyboards_admin = InlineKeyboardButton(text='👨‍💻 Администратор', callback_data='admin')
    keyboards_greeting_admin.row(keyboards_admin)
    return keyboards_greeting_admin


if __name__ == '__main__':
    greeting_keyboards()
    greeting_keyboards_admin()
