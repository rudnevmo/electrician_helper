from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from confige import telegram_bot_token


bot = Bot(token=telegram_bot_token)
dp = Dispatcher(bot)
