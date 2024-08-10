def count_norm_of_calories(user_info):
    if user_info['activity'] == "Сидячий образ жизни, никаких упражнений":
        kfa = 1
    elif user_info['activity'] == "Легкая активность (небольшие упражнения 1-3 раза в неделю)":
        kfa = 1.3
    else:
        kfa = 1.5
    if user_info['goal'] == "Набор массы":
        kc = 1.1
    elif user_info['goal'] == "Оставаться в форме":
        kc = 1
    else:
        kc = 0.9
    if user_info['gender'] == 'Женский':
        if 18 <= int(user_info['age']) <= 30:
            user_info['norm_of_calories'] = round((0.062 * float(user_info['weight']) + 2.036) * 240 * kfa * kc)
        elif 30 < int(user_info['age']) <= 60:
            user_info['norm_of_calories'] = round((0.034 * float(user_info['weight']) + 3.538) * 240 * kfa * kc)
        else:
            user_info['norm_of_calories'] = round((0.038 * float(user_info['weight']) + 2.755) * 240 * kfa * kc)
    else:
        if 18 <= int(user_info['age']) <= 30:
            user_info['norm_of_calories'] = round((0.063 * float(user_info['weight']) + 2.896) * 240 * kfa * kc)
        elif 30 < int(user_info['age']) <= 60:
            user_info['norm_of_calories'] = round((0.048 * float(user_info['weight']) + 3.653) * 240 * kfa * kc)
        else:
            user_info['norm_of_calories'] = round((0.049 * float(user_info['weight']) + 2.459) * 240 * kfa * kc)
    return user_info


def count_norm_of_pfc(user_info):
    proteins = round(float(user_info['weight']) * 1.75)
    fats = round(float(user_info['weight']) * 1.15)
    carbohydrates = round(float(user_info['weight']) * 2)
    user_info['norm_of_pfc'] = {
        "proteins": proteins,
        "fats": fats,
        "carbohydrates": carbohydrates
    }
    return user_info
