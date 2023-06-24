import configparser
import logging

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)
config.read("setting/config.ini")
BOT_TOKEN = config.get('BOT_TOKEN', 'BOT_TOKEN')
DELIVERY_BELARUS = config.get('DELIVERY_BELARUS', 'DELIVERY_BELARUS')
COMMISSION_BELARUS = config.get('COMMISSION_BELARUS', 'COMMISSION_BELARUS')

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
