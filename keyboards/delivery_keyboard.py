from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def delivery_keyboard_technics():
    """Клавиатура техники доставки"""
    technics_delivery_keyboard = InlineKeyboardMarkup()
    technics_aircraft_button = InlineKeyboardButton(text='Польский злотый', callback_data='polish_zloty')
    technics_accelerated_by_truck = InlineKeyboardButton(text='Евро', callback_data='euro')
    technics_a_regular_truck = InlineKeyboardButton(text='Юани', callback_data='yuan')
    technics_delivery_keyboard.row(technics_aircraft_button)
    technics_delivery_keyboard.row(technics_accelerated_by_truck, technics_a_regular_truck)
    return technics_delivery_keyboard


if __name__ == '__main__':
    delivery_keyboard_technics()
