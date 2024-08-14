import json
import datetime
from bot.config import data_dir
from bot.utils.read_and_write_functions import read_json,write_json

def check(message):
    user_info = read_json(message.chat.id)
    # if now time - water reminder time >= 24 hours, then update date for water and norm of water
    if (datetime.datetime.now() - datetime.datetime.strptime(user_info['date_for_water'], "%Y-%m-%d")).days >= 1:
        user_info['date_for_water'] = datetime.datetime.now().strftime("%Y-%m-%d")
        norm_of_water = float(user_info['weight']) * 0.03
        norm_of_water = round(norm_of_water * 4) / 4
        user_info['norm_of_water'] = norm_of_water - 0.25
        write_json(message.chat.id,user_info)
    else:
        user_info['norm_of_water'] -= 0.25
        write_json(message.chat.id,user_info)
    return user_info
