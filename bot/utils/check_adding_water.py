import json
import datetime
from bot.config import data_dir


def check(message):
    with open(f"{data_dir}/user_info_{message.chat.id}.json", 'r', encoding='utf-8') as file:
        user_info = json.load(file)
    # if now time - water reminder time >= 24 hours, then update date for water and norm of water
    if (datetime.datetime.now() - datetime.datetime.strptime(user_info['date_for_water'], "%Y-%m-%d")).days >= 1:
        user_info['date_for_water'] = datetime.datetime.now().strftime("%Y-%m-%d")
        norm_of_water = float(user_info['weight']) * 0.03
        norm_of_water = round(norm_of_water * 4) / 4
        user_info['norm_of_water'] = norm_of_water - 0.25
        with open(f"{data_dir}/user_info_{message.chat.id}.json", 'w', encoding='utf-8') as file:
            json.dump(user_info, file, ensure_ascii=False, indent=4)
    else:
        user_info['norm_of_water'] -= 0.25
        with open(f"{data_dir}/user_info_{message.chat.id}.json", 'w', encoding='utf-8') as file:
            json.dump(user_info, file, ensure_ascii=False, indent=4)
    return user_info
