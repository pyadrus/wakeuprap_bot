from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_panel_keyboard():
    """Клавиатура админа"""
    admin_keyboard = InlineKeyboardMarkup()
    change_order_status_button = InlineKeyboardButton(text='Изменить статус заказа',
                                                      callback_data='change_order_status')
    unload_orders_button = InlineKeyboardButton(text='Выгрузить заказы', callback_data='unload_orders')
    admin_keyboard.row(change_order_status_button, unload_orders_button)
    check_bot_users = InlineKeyboardButton(text='Проверить пользователей бота', callback_data='check_bot_users')
    admin_keyboard.row(check_bot_users)
    change_exchange_rate_button = InlineKeyboardButton(text='Изменить курс валют', callback_data='change_exchange_rate')
    admin_keyboard.row(change_exchange_rate_button)
    return admin_keyboard


def order_status():
    """Статус заказа"""
    order_status_keyboard = InlineKeyboardMarkup()
    in_processing_button = InlineKeyboardButton(text='В обработке', callback_data='in_processing')
    sent_button = InlineKeyboardButton(text='Отправлен', callback_data='sent')
    order_status_keyboard.row(in_processing_button, sent_button)
    cancelled_button = InlineKeyboardButton(text='Отменен', callback_data='cancelled')
    refund_button = InlineKeyboardButton(text='Возврат', callback_data='refund')
    order_status_keyboard.row(cancelled_button, refund_button)
    completed_button = InlineKeyboardButton(text='Завершен', callback_data='completed')
    order_status_keyboard.row(completed_button)
    return order_status_keyboard


if __name__ == '__main__':
    admin_panel_keyboard()
