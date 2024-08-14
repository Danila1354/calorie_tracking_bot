import json
import datetime
from .counter_functions import count_norm_of_calories, count_norm_of_pfc
from bot.config import data_dir
from bot.utils.read_and_write_functions import write_json

def save(data, message):
    norm_of_water = float(data['weight']) * 0.03
    norm_of_water = round(norm_of_water * 4) / 4
    user_info = {
        "gender": data['gender'],
        "age": data['age'],
        "weight": data['weight'],
        "goal": data['goal'],
        "activity": data['activity'],
        "water_reminder": "off",
        "norm_of_water": norm_of_water,
        "date_for_water": datetime.datetime.now().strftime("%Y-%m-%d"),
        "date_for_calories_and_pfc": datetime.datetime.now().strftime("%Y-%m-%d"),
        "calories": 0,
        "pfc": {
            "proteins": 0,
            "fats": 0,
            "carbohydrates": 0
        }
    }
    user_info = count_norm_of_calories(user_info)
    user_info = count_norm_of_pfc(user_info)

    write_json(message.chat.id,user_info)
