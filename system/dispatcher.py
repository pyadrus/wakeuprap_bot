import configparser
import logging

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)
config.read("setting/config.ini")
# Токен бота
BOT_TOKEN = config.get('BOT_TOKEN', 'BOT_TOKEN')

# Доставка и комиссия Россия
DELIVERY_RU_EUR = config.get('DELIVERY_RU_EUR', 'DELIVERY_RU_EUR')
DELIVERY_RU_YUAN_ACCESSORIES = config.get('DELIVERY_RU_YUAN_ACCESSORIES', 'DELIVERY_RU_YUAN')
DELIVERY_RU_YUAN_SHOES = config.get('DELIVERY_RU_YUAN_SHOES', 'DELIVERY_RU_YUAN')
DELIVERY_RU_YUAN_CLOTHING = config.get('DELIVERY_RU_YUAN_CLOTHING', 'DELIVERY_RU_YUAN')
COMMISSION_RU_EUR_YUAN = config.get('COMMISSION_RU_EUR_YUAN', 'COMMISSION_RU_EUR_YUAN')

# Доставка и комиссия Беларусь
DELIVERY_BY_YUAN_ACCESSORIES = config.get('DELIVERY_BY_YUAN_ACCESSORIES', 'DELIVERY_BY_YUAN')
DELIVERY_BY_YUAN_SHOES = config.get('DELIVERY_BY_YUAN_SHOES', 'DELIVERY_BY_YUAN')
DELIVERY_BY_YUAN_CLOTHING = config.get('DELIVERY_BY_YUAN_CLOTHING', 'DELIVERY_BY_YUAN')
DELIVERY_BY_EUR = config.get('DELIVERY_BELARUS', 'DELIVERY_BELARUS')
COMMISSION_BY_YUAN_EUR = config.get('COMMISSION_BY_YUAN_EUR', 'COMMISSION_BY_YUAN_EUR')

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
