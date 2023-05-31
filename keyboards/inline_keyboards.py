from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def greeting_keyboards():
    """Клавиатуры поста приветствия"""
    keyboards_greeting = InlineKeyboardMarkup()
    price_calculator = InlineKeyboardButton(text='🧮 Калькулятор цен', callback_data='price_calculator')
    contacts = InlineKeyboardButton(text='📇 Контакты', callback_data='contacts')
    faq = InlineKeyboardButton(text='Статьи FAQ', callback_data='faq')
    keyboards_greeting.row(price_calculator, contacts)
    keyboards_greeting.row(faq)
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
    technics = InlineKeyboardButton(text='📱 Техника', callback_data='technics')
    keyboard_clothes.row(footwear, trousers)  # Кнопка одежды
    keyboard_clothes.row(hoodies, down_jacket_button)  # Кнопка одежды
    keyboard_clothes.row(down_jacket_synthetic, backpack)  # Кнопка одежды
    keyboard_clothes.row(shoulder_bag, longsleeve)  # Кнопка одежды
    keyboard_clothes.row(technics)  # Inline кнопка техники
    return keyboard_clothes


def delivery_keyboard_technics():
    """Клавиатура техники доставки"""
    technics_delivery_keyboard = InlineKeyboardMarkup()
    technics_aircraft_button = InlineKeyboardButton(text='🚀 1-3 дня (рейсовый самолет)',
                                                    callback_data='technics_aircraft')
    technics_accelerated_by_truck = InlineKeyboardButton(text='🚛 8-15 дней (ускоренной фурой)',
                                                         callback_data='technics_accelerated_by_truck')
    technics_a_regular_truck = InlineKeyboardButton(text='🚚 20-30 дней (обычной фурой)',
                                                    callback_data='technics_a_regular_truck')
    technics_delivery_keyboard.row(technics_aircraft_button)
    technics_delivery_keyboard.row(technics_accelerated_by_truck)
    technics_delivery_keyboard.row(technics_a_regular_truck)
    return technics_delivery_keyboard


def delivery_keyboard():
    """Клавиатура доставки"""
    deliver_keyboard = InlineKeyboardMarkup()
    scheduled_aircraft_button = InlineKeyboardButton(text='🚀 1-3 дня (рейсовый самолет)',
                                                     callback_data='scheduled_aircraft')
    accelerated_by_truck = InlineKeyboardButton(text='🚛 8-15 дней (ускоренной фурой)',
                                                callback_data='accelerated_by_truck')
    a_regular_truck = InlineKeyboardButton(text='🚚 20-30 дней (обычной фурой)',
                                           callback_data='a_regular_truck')
    deliver_keyboard.row(scheduled_aircraft_button)
    deliver_keyboard.row(accelerated_by_truck)
    deliver_keyboard.row(a_regular_truck)
    return deliver_keyboard


if __name__ == '__main__':
    greeting_keyboards()
    clothing_keyboard()
    delivery_keyboard()
