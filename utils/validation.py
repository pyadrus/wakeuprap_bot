from services.exchange import get_currency_rate


def calculate_commission_price(price):
    """Расчет стоимости комиссии"""
    if price < 500:
        commission = 500  # Комиссия 500 рублей
    elif 500 <= price < 1000:
        commission = 750  # Комиссия 750 рублей
    elif 1000 <= price < 2000:
        commission = 1000  # Комиссия 1000 рублей
    elif price >= 2000:
        commission = price * 0.05  # 5% от стоимости заказа в рублях
    return commission


def calculate_insurance_price(price):
    """Расчет стоимости страховки"""
    cny_rate = get_currency_rate('CNY')  # Курс Юаня к рублю
    price_in_rubles = price * cny_rate  # Переводим введенную цену пользователем в рубли
    delivery_rub_cn = 30 * cny_rate  # Цена доставки Poizon до склада в Китай
    total_price_in_rubles = delivery_rub_cn + price_in_rubles  # Цена товара
    insurance_price = (0.2 * total_price_in_rubles) / total_price_in_rubles  # Страховка
    return insurance_price  # Возвращаем цену страховки
