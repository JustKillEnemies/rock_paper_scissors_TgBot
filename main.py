from config import load_config

from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


config = load_config()

bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()
