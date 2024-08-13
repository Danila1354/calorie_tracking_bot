from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.keyboards.keyboards import food_diary_kb, return_kb, food_diary_one_button_kb
from bot.states.fsm_classes import FormFood
from bot.utils.parse_pfc import parse_pfc
from bot.utils.check_adding_food import check
from bot.config import data_dir

import json


async def food_diary(message: types.Message):
    await message.answer("Дневник питания", reply_markup=food_diary_kb)


async def food_entry(message: types.Message):
    await message.answer("Запишите, что вы съели", reply_markup=return_kb)
    await FormFood.food.set()


async def food_entry_answer(message: types.Message, state: FSMContext):
    mes_del = await message.answer("Подождите, идет обработка запроса...")
    mes, result = parse_pfc(message.text)
    mes += 'Добавить в съеденное за сегодня?'
    with open(f'{data_dir}/user_info_{message.chat.id}.json', 'r', encoding='utf-8') as file:
        user_info = json.load(file)
    user_info['intermediate_result'] = result
    with open(f'{data_dir}/user_info_{message.chat.id}.json', 'w', encoding='utf-8') as file:
        json.dump(user_info, file, ensure_ascii=False, indent=4)
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Да")).row(
        types.KeyboardButton('Нет'))
    await mes_del.delete()
    await message.answer(mes, reply_markup=kb)
    await state.finish()


async def add_to_food_diary_yes(message: types.Message):
    user_info = check(message)
    await message.answer(f'За сегодня вы съели {user_info["calories"]}/{user_info["norm_of_calories"]} ккал\nБЖУ: '
                         f'{user_info["pfc"]["proteins"]}/{user_info["pfc"]["fats"]}/'
                         f'{user_info["pfc"]["carbohydrates"]} из {user_info["norm_of_pfc"]["proteins"]}/'
                         f'{user_info["norm_of_pfc"]["fats"]}/{user_info["norm_of_pfc"]["carbohydrates"]}',
                         reply_markup=food_diary_one_button_kb)


async def add_to_food_diary_no(message: types.Message):
    await message.answer("Запись не добавлена", reply_markup=food_diary_kb)


def register_handlers_food_diary(dp):
    dp.register_message_handler(food_diary, text='Дневник питания')
    dp.register_message_handler(food_entry, text='Записать приём пищи')
    dp.register_message_handler(food_entry_answer, state=FormFood.food)
    dp.register_message_handler(add_to_food_diary_yes, text='Да')
    dp.register_message_handler(add_to_food_diary_no, text='Нет')
