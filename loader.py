from aiogram import Dispatcher, types, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN_BOT


bot = Bot(token=TOKEN_BOT, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

