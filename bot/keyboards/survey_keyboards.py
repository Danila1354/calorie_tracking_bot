from aiogram import types

gender_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Мужской"),
                                                                types.KeyboardButton(text="Женский"))
survey_again_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(
    types.KeyboardButton(text="Заполнить анкету заново"))
goal_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Набор массы")).row(
    types.KeyboardButton(text="Оставаться в форме")).row(
    types.KeyboardButton(text="Снижение массы"), types.KeyboardButton('Заполнить анкету заново'))
activity_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(
    types.KeyboardButton(text="Сидячий образ жизни, никаких упражнений")).row(
    types.KeyboardButton(text='Легкая активность (небольшие '
                              'упражнения 1-3 раза в неделю)')).row(
    types.KeyboardButton(text='Высокая активность ('
                              'тренируюсь более 4-х раз в '
                              'неделю)')).row(types.KeyboardButton('Заполнить анкету заново'))
return_to_menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Главное меню"))
