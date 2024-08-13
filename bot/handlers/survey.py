from aiogram.dispatcher import FSMContext
from bot.states.fsm_classes import Form
from bot.keyboards.survey_keyboards import gender_kb, survey_again_kb, goal_kb, activity_kb, return_to_menu_kb
from aiogram import types
from bot.utils import save_information


async def form(message: types.Message):
    await message.answer("Какой у вас пол?", reply_markup=gender_kb)
    await Form.gender.set()


async def gender_answer(message: types.Message, state: FSMContext):
    if message.text not in ["Мужской", "Женский"]:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов")
        return
    async with state.proxy() as data:
        data['gender'] = message.text
    await message.answer("Сколько вам лет?", reply_markup=survey_again_kb)
    await Form.next()


async def age_answer(message: types.Message, state: FSMContext):
    if message.text == 'Заполнить анкету заново':
        await message.answer("Какой у вас пол?", reply_markup=gender_kb)
        await state.finish()
        await Form.gender.set()
        return
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите число")
        return
    async with state.proxy() as data:
        data['age'] = message.text
    await message.answer("Сколько вы весите (в кг)?", reply_markup=survey_again_kb)
    await Form.next()


async def weight_answer(message: types.Message, state: FSMContext):
    if message.text == 'Заполнить анкету заново':
        await message.answer("Какой у вас пол?", reply_markup=gender_kb)
        await state.finish()
        await Form.gender.set()
        return
    # check that message.text is int or float
    if not message.text.replace('.', '', 1).replace(',', '', 1).isdigit():
        await message.answer("Пожалуйста, введите число")
        return

    async with state.proxy() as data:
        data['weight'] = message.text
    await message.answer("Какая у вас цель?", reply_markup=goal_kb)
    await Form.next()


async def goal_answer(message: types.Message, state: FSMContext):
    if message.text == 'Заполнить анкету заново':
        await message.answer("Какой у вас пол?", reply_markup=gender_kb)
        await state.finish()
        await Form.gender.set()
        return
    if message.text not in ["Набор массы", "Оставаться в форме", "Снижение массы"]:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов")
        return
    async with state.proxy() as data:
        data['goal'] = message.text
    await message.answer("Опишите ваш уровень физической активности.", reply_markup=activity_kb)
    await Form.next()


async def activity_answer(message: types.Message, state: FSMContext):
    if message.text == 'Заполнить анкету заново':
        await message.answer("Какой у вас пол?", reply_markup=gender_kb)
        await state.finish()
        await Form.gender.set()
        return
    if message.text not in ["Сидячий образ жизни, никаких упражнений", "Легкая активность "
                                                                       "(небольшие упражнения 1-3 раза в неделю)",
                            "Высокая активность (тренируюсь более 4-х раз в неделю)"]:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов")
        return
    async with state.proxy() as data:
        data['activity'] = message.text
    # count norm of water, round to nearest number that divisible by 0.250
    save_information.save(data, message)
    await state.finish()
    await message.answer("Спасибо за предоставленную информацию!", reply_markup=return_to_menu_kb)


def register_handlers_survey(dp):
    dp.register_message_handler(form, text="Заполнить анкету")
    dp.register_message_handler(gender_answer, state=Form.gender)
    dp.register_message_handler(age_answer, state=Form.age)
    dp.register_message_handler(weight_answer, state=Form.weight)
    dp.register_message_handler(goal_answer, state=Form.goal)
    dp.register_message_handler(activity_answer, state=Form.activity)
