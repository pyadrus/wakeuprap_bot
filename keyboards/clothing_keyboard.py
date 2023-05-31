from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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


if __name__ == '__main__':
    clothing_keyboard()
