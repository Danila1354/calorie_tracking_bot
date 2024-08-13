from aiogram import types
import json

from aiogram.dispatcher import FSMContext
from bot.utils.counter_functions import count_norm_of_calories, count_norm_of_pfc
from bot.keyboards.keyboards import profile_kb, start_test_kb, change_profile_kb
from bot.states.fsm_classes import FormNewWeight
from bot.config import data_dir


async def profile(message: types.Message):
    try:
        with open(f"{data_dir}/user_info_{message.chat.id}.json", 'r', encoding='utf-8') as file:
            user_info = json.load(file)
        await message.answer(f"Ваш профиль:\n\n"
                             f"Пол: {user_info['gender']}\n"
                             f"Возраст: {user_info['age']}\n"
                             f"Вес: {user_info['weight']}\n"
                             f"Цель: {user_info['goal']}\n"
                             f"Активность: {user_info['activity']}", reply_markup=profile_kb)
    except FileNotFoundError:
        await message.answer("У вас нет профиля. Пожалуйста, заполните анкету", reply_markup=start_test_kb)


async def edit_profile(message: types.Message):
    await message.answer("Чтобы изменить профиль, заполните заново анкету", reply_markup=change_profile_kb)


async def weight_change(message: types.Message):
    await message.answer("Введите ваш новый вес", reply_markup=types.ReplyKeyboardRemove())
    await FormNewWeight.new_weight.set()


async def weight_change_answer(message: types.Message, state: FSMContext):
    if not message.text.replace('.', '', 1).replace(',', '', 1).isdigit():
        await message.answer("Пожалуйста, введите число")
        return
    async with state.proxy() as data:
        data['new_weight'] = message.text
    with open(f"{data_dir}/user_info_{message.chat.id}.json", 'r', encoding='utf-8') as file:
        user_info = json.load(file)
    user_info['weight'] = data['new_weight']
    user_info = count_norm_of_calories(user_info)
    user_info = count_norm_of_pfc(user_info)
    with open(f"{data_dir}/user_info_{message.chat.id}.json", 'w', encoding='utf-8') as file:
        json.dump(user_info, file, ensure_ascii=False, indent=4)
    await state.finish()
    await message.answer("Ваш вес успешно изменен", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).row(
        types.KeyboardButton(text="Назад"))
                         )


def register_handlers_profile(dp):
    dp.register_message_handler(profile, text='Профиль')
    dp.register_message_handler(edit_profile, text='Изменить профиль')
    dp.register_message_handler(weight_change, text='Записать изменение веса')
    dp.register_message_handler(weight_change_answer, state=FormNewWeight.new_weight)
