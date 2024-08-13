from aiogram import types
import json
from bot.keyboards.keyboards import water_remind_kb_on, water_remind_kb_off, food_diary_one_button_kb
from bot.utils.check_adding_water import check
from bot.config import data_dir


async def reminder(message: types.Message):
    with open(f"{data_dir}/user_info_{message.chat.id}.json", 'r', encoding='utf-8') as file:
        user_info = json.load(file)
    if user_info['water_reminder'] == "off":
        await message.answer("Напоминания о воде выключены", reply_markup=water_remind_kb_on)
    else:
        await message.answer("Напоминания о воде включены", reply_markup=water_remind_kb_off)


async def reminder_on(message: types.Message):
    with open(f"{data_dir}/user_info_{message.chat.id}.json", 'r', encoding='utf-8') as file:
        user_info = json.load(file)
    user_info['water_reminder'] = "on"
    with open(f"{data_dir}/user_info_{message.chat.id}.json", 'w', encoding='utf-8') as file:
        json.dump(user_info, file, ensure_ascii=False, indent=4)
    await message.answer("Напоминания о воде включены", reply_markup=water_remind_kb_off)


async def reminder_off(message: types.Message):
    with open(f"{data_dir}/user_info_{message.chat.id}.json", 'r', encoding='utf-8') as file:
        user_info = json.load(file)
    user_info['water_reminder'] = "off"
    with open(f"{data_dir}/user_info_{message.chat.id}.json", 'w', encoding='utf-8') as file:
        json.dump(user_info, file, ensure_ascii=False, indent=4)
    await message.answer("Напоминания о воде выключены", reply_markup=water_remind_kb_on)


async def drink_glass(message: types.Message):
    user_info = check(message)
    remaining = user_info['norm_of_water'] / 0.25
    await message.answer(f"Вы выпили стакан воды. Вам осталось выпить {user_info['norm_of_water']}л воды или "
                         f" {remaining} стаканов на сегодня.",
                         reply_markup=food_diary_one_button_kb)


def register_handlers_water_remind(dp):
    dp.register_message_handler(reminder, text="Напоминание")
    dp.register_message_handler(reminder_on, text="Включить")
    dp.register_message_handler(reminder_off, text="Выключить")
    dp.register_message_handler(drink_glass, text="Выпить стакан")
