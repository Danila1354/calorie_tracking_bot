from aiogram import types
from bot.keyboards.keyboards import start_kb, main_menu_kb


async def start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}, я бот, призванный помочь тебе создать и поддерживать "
        f"твоё тело "
        f"здоровым, "
        f"а в здоровом теле - здоровый дух", reply_markup=start_kb)


async def main_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Профиль")).row(
        types.KeyboardButton('Дневник питания')).row(types.KeyboardButton('Напоминание'))
    await message.answer("Главное меню", reply_markup=main_menu_kb)


def register_handlers_start(dp):
    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(main_menu, text=["Главное меню", "Назад"])
