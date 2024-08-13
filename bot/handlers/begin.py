import os
from aiogram import types
from bot.keyboards.keyboards import main_menu_kb, start_test_kb
from bot.config import data_dir


async def begin(message: types.Message):
    if os.path.exists(f"{data_dir}/user_info_{message.chat.id}.json"):
        await message.answer("Главное меню", reply_markup=main_menu_kb)
    else:
        await message.answer("У меня нет ваших данных. Пожалуйста, заполните анкету", reply_markup=start_test_kb)


def register_handlers_begin(dp):
    dp.register_message_handler(begin, text='Начать')
