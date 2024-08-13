from aiogram import types
from bot.config import admins_id
from bot.keyboards.keyboards import admin_kb, return_kb
from bot.states.fsm_classes import AdminForm
import os
from aiogram.dispatcher import FSMContext
from bot.config import data_dir


async def admin(message: types.Message):
    if message.chat.id in admins_id:
        await message.answer("Админ панель", reply_markup=admin_kb)
    else:
        await message.answer("У вас нет прав администратора")


async def mailing(message: types.Message):
    if message.chat.id in admins_id:
        await message.answer("Введите текст рассылки", reply_markup=types.ReplyKeyboardRemove())
        await AdminForm.text.set()
    else:
        await message.answer("У вас нет прав администратора")


async def mailing_answer(message: types.Message, state: FSMContext):
    for user in os.listdir(f'{data_dir}'):
        user = user.split('_')[-1].split('.')[0]
        try:
            await bot.send_message(user, message.text)
        except Exception as e:
            print(f"Failed to send message to user {message.chat.id}: {e}")
    await state.finish()
    await message.answer("Рассылка завершена", reply_markup=return_kb)


def register_handlers_admin(dp):
    dp.register_message_handler(admin, commands=['admin'])
    dp.register_message_handler(mailing, text='Сделать рассылку')
    dp.register_message_handler(mailing_answer, state=AdminForm.text)
