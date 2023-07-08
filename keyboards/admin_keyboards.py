from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_panel_keyboard():
    """Клавиатура админа"""
    admin_keyboard = InlineKeyboardMarkup()
    change_order_status_button = InlineKeyboardButton(text='Статус заказа',
                                                      callback_data='change_order_status')
    change_exchange_rate_button = InlineKeyboardButton(text='Изменить курс валют', callback_data='change_exchange_rate')
    admin_keyboard.row(change_order_status_button, change_exchange_rate_button)

    unload_orders_button = InlineKeyboardButton(text='Выгрузить заказы', callback_data='unload_orders')
    check_bot_users = InlineKeyboardButton(text='Выгрузить users', callback_data='check_bot_users')
    admin_keyboard.row(unload_orders_button, check_bot_users)

    make_an_order_keyboards = InlineKeyboardButton(text='🔥 Оформить заказ 🔥 ', callback_data='make_an_order')
    admin_keyboard.row(make_an_order_keyboards)

    calculate_order_amount_keyboards = InlineKeyboardButton(text='💵 Рассчитать стоимость', callback_data='calculate_order_amount')
    # Пользователь добавляет трек номер и получает данные
    admin_keyboard.row(calculate_order_amount_keyboards)

    return admin_keyboard


def order_status():
    """Статус заказа"""
    order_status_keyboard = InlineKeyboardMarkup()
    in_processing_button = InlineKeyboardButton(text='Ожидается на складе', callback_data='in_processing')
    order_status_keyboard.row(in_processing_button)
    sent_button = InlineKeyboardButton(text='Заказ прибыл на склад и отправлен в Минск', callback_data='sent')
    order_status_keyboard.row(sent_button)
    cancelled_button = InlineKeyboardButton(text='Заказ прибыл на склад в Минске', callback_data='cancelled')
    order_status_keyboard.row(cancelled_button)
    refund_button = InlineKeyboardButton(text='Заказ получен', callback_data='refund')
    order_status_keyboard.row(refund_button)
    return order_status_keyboard


def currency_exchange_rate_keyboard():
    """Клавиатура курса валют Белорусский рубль к Польскому злотому, Евро, Юани
                                  Русский рубль к Польскому злотому, Евро, Юани"""
    cur_exchange_rate_keyboard = InlineKeyboardMarkup()
    byn_pln_button = InlineKeyboardButton(text='BYN / PLN', callback_data='byn_pln_button')
    byn_eur_button = InlineKeyboardButton(text='BYN / EUR', callback_data='byn_eur_button')
    byn_yuan_button = InlineKeyboardButton(text='BYN / YUAN', callback_data='byn_yuan_button')
    cur_exchange_rate_keyboard.row(byn_pln_button, byn_eur_button, byn_yuan_button)
    rub_pln_button = InlineKeyboardButton(text='RUB / PLN', callback_data='rub_pln_button')
    rub_eur_button = InlineKeyboardButton(text='RUB / EUR', callback_data='rub_eur_button')
    rub_yuan_button = InlineKeyboardButton(text='RUB / YUAN', callback_data='rub_yuan_button')
    cur_exchange_rate_keyboard.row(rub_pln_button, rub_eur_button, rub_yuan_button)
    return cur_exchange_rate_keyboard


if __name__ == '__main__':
    admin_panel_keyboard()
    order_status()
    currency_exchange_rate_keyboard()
