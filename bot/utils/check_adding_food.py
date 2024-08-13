import datetime
import json
from bot.config import data_dir


def check(message):
    with open(f'{data_dir}/user_info_{message.chat.id}.json', 'r', encoding='utf-8') as file:
        user_info = json.load(file)

    # if now time - date for calories and pfc >= 24 hours, then update date for calories and pfc
    if ((datetime.datetime.now() - datetime.datetime.strptime(user_info['date_for_calories_and_pfc'], "%Y-%m-%d")).days
            >= 1):
        user_info['date_for_calories_and_pfc'] = datetime.datetime.now().strftime("%Y-%m-%d")
        user_info['calories'] = user_info['intermediate_result']['sum_calories']
        user_info['pfc']['proteins'] = user_info['intermediate_result']['sum_protein']
        user_info['pfc']['fats'] = user_info['intermediate_result']['sum_fat']
        user_info['pfc']['carbohydrates'] = user_info['intermediate_result']['sum_carbohydrate']
        with open(f'{data_dir}/user_info_{message.chat.id}.json', 'w', encoding='utf-8') as file:
            json.dump(user_info, file, ensure_ascii=False, indent=4)
    else:
        user_info['calories'] += user_info['intermediate_result']['sum_calories']
        user_info['pfc']['proteins'] += user_info['intermediate_result']['sum_protein']
        user_info['pfc']['fats'] += user_info['intermediate_result']['sum_fat']
        user_info['pfc']['carbohydrates'] += user_info['intermediate_result']['sum_carbohydrate']
        with open(f'{data_dir}/user_info_{message.chat.id}.json', 'w', encoding='utf-8') as file:
            json.dump(user_info, file, ensure_ascii=False, indent=4)
    return user_info
