# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
#
# def delivery_keyboard_technics():
#     """Клавиатура техники доставки"""
#     technics_delivery_keyboard = InlineKeyboardMarkup()
#     technics_aircraft_button = InlineKeyboardButton(text='🚀 1-3 дня (рейсовый самолет)',
#                                                     callback_data='technics_aircraft')
#     technics_accelerated_by_truck = InlineKeyboardButton(text='🚛 8-15 дней (ускоренной фурой)',
#                                                          callback_data='technics_accelerated_by_truck')
#     technics_a_regular_truck = InlineKeyboardButton(text='🚚 20-30 дней (обычной фурой)',
#                                                     callback_data='technics_a_regular_truck')
#     technics_delivery_keyboard.row(technics_aircraft_button)
#     technics_delivery_keyboard.row(technics_accelerated_by_truck)
#     technics_delivery_keyboard.row(technics_a_regular_truck)
#     return technics_delivery_keyboard
#
#
# def delivery_keyboard():
#     """Клавиатура доставки"""
#     deliver_keyboard = InlineKeyboardMarkup()
#     scheduled_aircraft_button = InlineKeyboardButton(text='🚀 1-3 дня (рейсовый самолет)',
#                                                      callback_data='scheduled_aircraft')
#     accelerated_by_truck = InlineKeyboardButton(text='🚛 8-15 дней (ускоренной фурой)',
#                                                 callback_data='accelerated_by_truck')
#     a_regular_truck = InlineKeyboardButton(text='🚚 20-30 дней (обычной фурой)',
#                                            callback_data='a_regular_truck')
#     deliver_keyboard.row(scheduled_aircraft_button)
#     deliver_keyboard.row(accelerated_by_truck)
#     deliver_keyboard.row(a_regular_truck)
#     return deliver_keyboard
#
#
# if __name__ == '__main__':
#     delivery_keyboard()
