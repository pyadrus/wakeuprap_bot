from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def clothing_keyboard():
    """Клавиатура одежды"""
    keyboard_clothes = InlineKeyboardMarkup()
    down_jacket_button = InlineKeyboardButton(text='🧥 Пуховик (пух)', callback_data='down_jacket_down')
    keyboard_clothes.row(down_jacket_button)
    return keyboard_clothes


def delivery_keyboard():
    """Клавиатура доставки"""
    delivery_keyboard = InlineKeyboardMarkup()
    scheduled_aircraft_button = InlineKeyboardButton(text='🚀 Опция "1-3 дня"', callback_data='scheduled_aircraft')
    accelerated_by_truck = InlineKeyboardButton(text='🚛 Опция "8-15 дней"', callback_data='accelerated_by_truck')
    a_regular_truck = InlineKeyboardButton(text='🚚 Опция "20-30 дней"', callback_data='a_regular_truck')
    delivery_keyboard.row(scheduled_aircraft_button)
    delivery_keyboard.row(accelerated_by_truck)
    delivery_keyboard.row(a_regular_truck)
    return delivery_keyboard


if __name__ == '__main__':
    clothing_keyboard()
    delivery_keyboard()
