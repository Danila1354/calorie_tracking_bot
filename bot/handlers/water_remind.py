from aiogram import types
import json
from bot.keyboards.keyboards import water_remind_kb_on, water_remind_kb_off, food_diary_one_button_kb
from bot.utils.check_adding_water import check
from bot.config import data_dir
from bot.utils.read_and_write_functions import read_json,write_json


async def reminder(message: types.Message):
    user_info = read_json(message.chat.id)
    if user_info['water_reminder'] == "off":
        await message.answer("Напоминания о воде выключены", reply_markup=water_remind_kb_on)
    else:
        await message.answer("Напоминания о воде включены", reply_markup=water_remind_kb_off)


async def reminder_on(message: types.Message):
    user_info = read_json(message.chat.id)
    user_info['water_reminder'] = "on"
    write_json(message.chat.id,user_info)
    await message.answer("Напоминания о воде включены", reply_markup=water_remind_kb_off)


async def reminder_off(message: types.Message):

    user_info = read_json(message.chat.id)
    user_info['water_reminder'] = "off"
    write_json(message.chat.id,user_info)
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
