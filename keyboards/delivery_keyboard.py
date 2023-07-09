from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def country_delivery_keyboard():
    """Выбор страны доставки"""
    delivery_keyboard = InlineKeyboardMarkup()
    delivery_keyboard_belarus = InlineKeyboardButton(text='🇧🇾 Беларусь', callback_data='belarus')
    delivery_keyboard_russia = InlineKeyboardButton(text='🇷🇺 Россия', callback_data='russia')
    delivery_keyboard.row(delivery_keyboard_belarus, delivery_keyboard_russia)
    return delivery_keyboard


def delivery_keyboard_technics_ru():
    """Клавиатура выбора валюты"""
    technics_delivery_keyboard = InlineKeyboardMarkup()
    technics_aircraft_button = InlineKeyboardButton(text='🇵🇱 Польский злотый', callback_data='polish_zloty_ru')
    technics_accelerated_by_truck = InlineKeyboardButton(text='🇪🇺 Евро', callback_data='euro_ru')
    technics_a_regular_truck = InlineKeyboardButton(text='🇨🇳 Юани', callback_data='yuan_ru')
    technics_delivery_keyboard.row(technics_aircraft_button)
    technics_delivery_keyboard.row(technics_accelerated_by_truck, technics_a_regular_truck)
    return technics_delivery_keyboard


def product_category_by_russia_polish_zloty_ru_keyboard():
    """Выбор категории товара"""
    product_category_keyboard = InlineKeyboardMarkup()
    accessories = InlineKeyboardButton(text='📱 Аксессуары', callback_data='accessories_ru_polish_zloty')
    shoes = InlineKeyboardButton(text='👟 Обувь', callback_data='shoes_ru_polish_zloty')
    clothing = InlineKeyboardButton(text='👔 Одежда', callback_data='clothing_ru_polish_zloty')
    product_category_keyboard.row(accessories, shoes, clothing)
    return product_category_keyboard


def product_category_by_russia_yuan_ru_keyboard():
    """Выбор категории товара для Китайского юаня"""
    product_category_keyboard = InlineKeyboardMarkup()
    accessories = InlineKeyboardButton(text='📱 Аксессуары', callback_data='accessories_ru_yuan')
    shoes = InlineKeyboardButton(text='👟 Обувь', callback_data='shoes_ru_yuan')
    clothing = InlineKeyboardButton(text='👔 Одежда', callback_data='clothing_ru_yuan')
    product_category_keyboard.row(accessories, shoes, clothing)
    return product_category_keyboard


def product_category_by_russia_euro_ru_keyboard():
    """Выбор категории товара"""
    product_category_keyboard = InlineKeyboardMarkup()
    accessories = InlineKeyboardButton(text='📱 Аксессуары', callback_data='accessories_ru_euro')
    shoes = InlineKeyboardButton(text='👟 Обувь', callback_data='shoes_ru_euro')
    clothing = InlineKeyboardButton(text='👔 Одежда', callback_data='clothing_ru_euro')
    product_category_keyboard.row(accessories, shoes, clothing)
    return product_category_keyboard


def delivery_keyboard_technics_by():
    """Клавиатура выбора валюты"""
    technics_delivery_keyboard = InlineKeyboardMarkup()
    technics_aircraft_button = InlineKeyboardButton(text='🇵🇱 Польский злотый', callback_data='polish_zloty_by')
    technics_accelerated_by_truck = InlineKeyboardButton(text='🇪🇺 Евро', callback_data='euro_by')
    technics_a_regular_truck = InlineKeyboardButton(text='🇨🇳 Юани', callback_data='yuan_by')
    technics_delivery_keyboard.row(technics_aircraft_button)
    technics_delivery_keyboard.row(technics_accelerated_by_truck, technics_a_regular_truck)
    return technics_delivery_keyboard


def product_category_by_russia_polish_zloty_by_keyboard():
    """Выбор категории товара"""
    product_category_keyboard = InlineKeyboardMarkup()
    accessories = InlineKeyboardButton(text='📱 Аксессуары', callback_data='accessories_by_polish_zloty')
    shoes = InlineKeyboardButton(text='👟 Обувь', callback_data='shoes_by_polish_zloty')
    clothing = InlineKeyboardButton(text='👔 Одежда', callback_data='clothing_by_polish_zloty')
    product_category_keyboard.row(accessories, shoes, clothing)
    return product_category_keyboard


def product_category_by_russia_yuan_by_keyboard():
    """Выбор категории товара для Китайского юаня"""
    product_category_keyboard = InlineKeyboardMarkup()
    accessories = InlineKeyboardButton(text='📱 Аксессуары', callback_data='accessories_by_yuan')
    shoes = InlineKeyboardButton(text='👟 Обувь', callback_data='shoes_by_yuan')
    clothing = InlineKeyboardButton(text='👔 Одежда', callback_data='clothing_by_yuan')
    product_category_keyboard.row(accessories, shoes, clothing)
    return product_category_keyboard


def product_category_by_russia_euro_by_keyboard():
    """Выбор категории товара"""
    product_category_keyboard = InlineKeyboardMarkup()
    accessories = InlineKeyboardButton(text='📱 Аксессуары', callback_data='accessories_by_euro')
    shoes = InlineKeyboardButton(text='👟 Обувь', callback_data='shoes_by_euro')
    clothing = InlineKeyboardButton(text='👔 Одежда', callback_data='clothing_by_euro')
    product_category_keyboard.row(accessories, shoes, clothing)
    return product_category_keyboard


if __name__ == '__main__':
    delivery_keyboard_technics_ru()
    country_delivery_keyboard()
    product_category_by_russia_polish_zloty_ru_keyboard()
    product_category_by_russia_euro_ru_keyboard()
    product_category_by_russia_yuan_ru_keyboard()
    delivery_keyboard_technics_by()
    product_category_by_russia_polish_zloty_by_keyboard()
    product_category_by_russia_euro_by_keyboard()
    product_category_by_russia_yuan_by_keyboard()
