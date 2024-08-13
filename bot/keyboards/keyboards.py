from aiogram import types

start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Начать"))
main_menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Профиль")).row(
    types.KeyboardButton('Дневник питания')).row(types.KeyboardButton('Напоминание'))
start_test_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Заполнить анкету"))
return_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Назад"))


profile_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton('Изменить профиль')).row(
    types.KeyboardButton('Записать изменение веса')).row(types.KeyboardButton('Назад'))
change_profile_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(
    types.KeyboardButton(text="Заполнить анкету")).row(
    types.KeyboardButton('Назад'))


food_diary_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Выпить стакан")).row(
    types.KeyboardButton('Записать приём пищи')).row(types.KeyboardButton('Назад'))
food_diary_one_button_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Дневник "
                                                                                                         "питания"))


admin_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Сделать рассылку")).row(
    'Назад')


water_remind_kb_on = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Включить")).row(
    types.KeyboardButton('Назад'))
water_remind_kb_off = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton(text="Выключить")).row(
    types.KeyboardButton('Назад'))
