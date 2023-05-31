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


if __name__ == '__main__':
    greeting_keyboards()
