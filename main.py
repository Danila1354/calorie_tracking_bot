from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot.config import TOKEN
import os
from bot.handlers import register_all_handlers

os.makedirs('data/users', exist_ok=True)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
# register all handlers
register_all_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
