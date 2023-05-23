import requests


def get_exchange_rates():
    """Получаем курс валют от ЦБ РФ"""
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()
    return data['Valute']


def get_currency_rate(currency_code):
    rates = get_exchange_rates()
    if currency_code == 'USD':
        return rates['USD']['Value']
    elif currency_code == 'CNY':
        return rates['CNY']['Value']
    else:
        return None


# usd_rate = get_currency_rate('USD')
# cny_rate = get_currency_rate('CNY')
