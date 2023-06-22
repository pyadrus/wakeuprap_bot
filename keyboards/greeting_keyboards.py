from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def greeting_keyboards():
    """Клавиатуры поста приветствия"""
    keyboards_greeting = InlineKeyboardMarkup()

    # price_calculator = InlineKeyboardButton(text='🧮 Калькулятор цен', callback_data='price_calculator')
    # contacts = InlineKeyboardButton(text='📇 Контакты', callback_data='contacts')  # Контакты
    # making_an_order = InlineKeyboardButton(text='🛒 Заказать', callback_data='making_an_order')  # Заказать товар
    # faq = InlineKeyboardButton(text='Статьи FAQ', callback_data='faq')
    # keyboards_greeting.row(price_calculator, contacts)
    # keyboards_greeting.row(making_an_order)
    make_an_order_keyboards = InlineKeyboardButton(text='🔥 Сделать заказ 🔥', callback_data='make_an_order')
    keyboards_greeting.row(make_an_order_keyboards)
    my_orders_keyboards = InlineKeyboardButton(text='📦 Мои заказы', callback_data='my_orders')
    add_a_track_number_keyboards = InlineKeyboardButton(text='➕ Добавить трек+номер', callback_data='add_track_number')
    keyboards_greeting.row(my_orders_keyboards, add_a_track_number_keyboards)
    yuan_exchange_rate_keyboards = InlineKeyboardButton(text='💹 Курс юаня 💹', callback_data='yuan_exchange_rate_keyboards')
    calculate_order_amount_keyboards = InlineKeyboardButton(text='💵 Рассчитать сумму заказа 💵', callback_data='calculate_order_amount')
    keyboards_greeting.row(yuan_exchange_rate_keyboards, calculate_order_amount_keyboards)
    product_selection_application = InlineKeyboardButton(text='📱 Приложение для выбора товара 📱', callback_data='product_selection_application')
    keyboards_greeting.row(product_selection_application)
    products_in_stock_application = InlineKeyboardButton(text='Товары в наличии 👟', callback_data='products_in_stock')
    chat_and_reviews_application = InlineKeyboardButton(text='🗣 Чат и отзывы 📝', callback_data='chat_and_reviews')
    keyboards_greeting.row(products_in_stock_application, chat_and_reviews_application)
    answers_to_the_main_questions_keyboards = InlineKeyboardButton(text='📍 Ответы на основные вопросы 📍', callback_data='answers_to_the_main_questions')
    keyboards_greeting.row(answers_to_the_main_questions_keyboards)
    return keyboards_greeting


if __name__ == '__main__':
    greeting_keyboards()
