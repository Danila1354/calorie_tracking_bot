import datetime
import json
from bot.config import data_dir
from bot.utils.read_and_write_functions import read_json,write_json

def check(message):
    user_info = read_json(message.chat.id)

    # if now time - date for calories and pfc >= 24 hours, then update date for calories and pfc
    if ((datetime.datetime.now() - datetime.datetime.strptime(user_info['date_for_calories_and_pfc'], "%Y-%m-%d")).days
            >= 1):
        user_info['date_for_calories_and_pfc'] = datetime.datetime.now().strftime("%Y-%m-%d")
        user_info['calories'] = user_info['intermediate_result']['sum_calories']
        user_info['pfc']['proteins'] = user_info['intermediate_result']['sum_protein']
        user_info['pfc']['fats'] = user_info['intermediate_result']['sum_fat']
        user_info['pfc']['carbohydrates'] = user_info['intermediate_result']['sum_carbohydrate']
        write_json(message.chat.id,user_info)
    else:
        user_info['calories'] += user_info['intermediate_result']['sum_calories']
        user_info['pfc']['proteins'] += user_info['intermediate_result']['sum_protein']
        user_info['pfc']['fats'] += user_info['intermediate_result']['sum_fat']
        user_info['pfc']['carbohydrates'] += user_info['intermediate_result']['sum_carbohydrate']
        write_json(message.chat.id,user_info)
    return user_info
