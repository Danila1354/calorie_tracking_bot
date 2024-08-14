from bot.config import data_dir
import json


def read_json(chat_id):
    with open(f'{data_dir}/user_info_{chat_id}.json', 'r', encoding='utf-8') as file:
        user_info = json.load(file)
    return user_info


def write_json(chat_id,user_info):
    with open(f'{data_dir}/user_info_{chat_id}.json', 'w', encoding='utf-8') as file:
        json.dump(user_info, file, ensure_ascii=False, indent=4)