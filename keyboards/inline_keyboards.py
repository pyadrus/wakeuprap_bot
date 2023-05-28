from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def greeting_keyboards():
    """Клавиатуры поста приветствия"""
    keyboards_greeting = InlineKeyboardMarkup()
    price_calculator = InlineKeyboardButton(text='🧮 Калькулятор цен', callback_data='price_calculator')
    contacts = InlineKeyboardButton(text='📇 Контакты', callback_data='contacts')
    keyboards_greeting.row(price_calculator, contacts)
    return keyboards_greeting


def clothing_keyboard():
    """Клавиатура одежды"""
    keyboard_clothes = InlineKeyboardMarkup()
    footwear = InlineKeyboardButton(text='👟 Обувь', callback_data='footwear')
    trousers = InlineKeyboardButton(text='👖 Штаны', callback_data='trousers')
    hoodies = InlineKeyboardButton(text='🥼 Худи', callback_data='hoodies')
    down_jacket_button = InlineKeyboardButton(text='🧥 Пуховик (пух)', callback_data='down_jacket_down')
    down_jacket_synthetic = InlineKeyboardButton(text='🧥 Пуховик (синтетика)', callback_data='down_jacket_synthetic')
    backpack = InlineKeyboardButton(text='🎒 Рюкзак', callback_data='backpack')
    shoulder_bag = InlineKeyboardButton(text='👜 Сумка наплечная', callback_data='shoulder_bag')
    longsleeve = InlineKeyboardButton(text='👕 Лонгслив / майка', callback_data='longsleeve')
    keyboard_clothes.row(footwear, trousers)
    keyboard_clothes.row(hoodies, down_jacket_button)
    keyboard_clothes.row(down_jacket_synthetic, backpack)
    keyboard_clothes.row(shoulder_bag, longsleeve)
    return keyboard_clothes


def delivery_keyboard():
    """Клавиатура доставки"""
    delivery_keyboard = InlineKeyboardMarkup()
    scheduled_aircraft_button = InlineKeyboardButton(text='🚀 1-3 дня (рейсовый самолет)"', callback_data='scheduled_aircraft')
    accelerated_by_truck = InlineKeyboardButton(text='🚛 8-15 дней (ускоренной фурой)"', callback_data='accelerated_by_truck')
    a_regular_truck = InlineKeyboardButton(text='🚚 20-30 дней (обычной фурой)"', callback_data='a_regular_truck')
    delivery_keyboard.row(scheduled_aircraft_button)
    delivery_keyboard.row(accelerated_by_truck)
    delivery_keyboard.row(a_regular_truck)
    return delivery_keyboard


if __name__ == '__main__':
    greeting_keyboards()
    clothing_keyboard()
    delivery_keyboard()
