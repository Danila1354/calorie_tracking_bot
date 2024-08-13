from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    gender = State()
    age = State()
    weight = State()
    goal = State()
    activity = State()


class FormNewWeight(StatesGroup):
    new_weight = State()


class FormFood(StatesGroup):
    food = State()


class AdminForm(StatesGroup):
    text = State()
