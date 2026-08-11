# Проект FitLife - MVP версия 1.0


# 1. Знакомство
print('=' * 70)
print('Здравствуйте! Вас приветствует программа FitLife')
user_name = input('Введите имя: ')

print(user_name, end=', ')
print('добро пожаловать!', end=', ')

user_age = int(input('Сколько вам лет? '))

print('.' * 70)
print(f'Ваш возраст {user_age}. Приятно познакомиться, {user_name}!')
print('Наша фитнес-программа поможет Вам укрепить и поддержать здоровье.')
print('Нам потребуются некоторые данные о Вашем физическом состоянии.')

# 2. Сбор данных
user_weight = float(input('Какой у вас вес (в килограммах)? '))

user_height = float(input('Укажите рост в метрах. Разделяйте точкой: "1.75" '))

# 3. Логика расчетов


def index_bmi(weight_kg, height_m):
    """рассчитываем индекс ИМТ"""
    bmi_output = weight_kg / (height_m ** 2)
    bmi_round = round(bmi_output, 1)
    return bmi_round


def volume_water(weight_kg):
    """рассчитываем норму объёма воды"""
    water_ml = weight_kg * 30
    water_l = water_ml / 1000
    water_l_round = round(water_l)
    return water_l_round


bmi = index_bmi(user_weight, user_height)  # Индекс Массы Тела пользователя
water = volume_water(user_weight)  # норма объёма воды пользователя

# 4. Вывод красивого результата
print('=' * 70)
print(f'Отчёт для пользователя {user_name} (возраст: {user_age})')
print(f'Ваш Индекс Массы Тела (ИМТ): {bmi}')
print(f'Рекомендуемая норма воды: {water} л. в день')
print("Расчет окончен. Будьте здоровы!")
print('.' * 70)
