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
    in_processing_button = InlineKeyboardButton(text='Ожидается на складе', callback_data='in_processing')
    order_status_keyboard.row(in_processing_button)
    sent_button = InlineKeyboardButton(text='Заказ прибыл на склад и отправлен в Минск', callback_data='sent')
    order_status_keyboard.row(sent_button)
    cancelled_button = InlineKeyboardButton(text='Заказ прибыл на склад в Минске', callback_data='cancelled')
    order_status_keyboard.row(cancelled_button)
    refund_button = InlineKeyboardButton(text='Заказ получен', callback_data='refund')
    order_status_keyboard.row(refund_button)
    return order_status_keyboard


if __name__ == '__main__':
    admin_panel_keyboard()
