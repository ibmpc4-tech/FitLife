# Проект FitLife - MVP версия 1.0

SEPARATOR_WIDTH = 70
ML_PER_KG = 30          # сколько миллилитров воды на 1 кг веса
ML_TO_LITERS = 1000     # сколько мл в одном литре

# 1. Знакомство
print('=' * SEPARATOR_WIDTH)
print('Здравствуйте! Вас приветствует программа FitLife')

user_name = input('Введите Ваше имя: ')

print(f'{user_name}, добро пожаловать!')

user_age = int(input('Сколько вам полных лет? (целое число): '))

print(
    f'{"." * SEPARATOR_WIDTH}\n'
    f'Ваш возраст {user_age}. Приятно познакомиться, {user_name}!\n'
    f'Наша фитнес-программа поможет Вам укрепить и поддержать здоровье.\n'
    f'Нам потребуются некоторые данные о Вашем физическом состоянии.',
)

# 2. Сбор данных
weight_input = input('Какой у вас вес? (в килограммах): ')
user_weight = float(weight_input.replace(',', '.'))  # вес

height_input = input('Какой у вас рост? [Пример: 1.73] (ТОЛЬКО в метрах): ')
user_height = float(height_input.replace(',', '.'))  # рост

# 3. Логика расчетов
bmi = user_weight / (user_height ** 2)  # ИМТ
water = (user_weight * ML_PER_KG) / ML_TO_LITERS  # вода

# 4. Вывод красивого результата
print(
    f'{"=" * SEPARATOR_WIDTH}\n'
    f'Отчёт для пользователя {user_name} (возраст: {user_age})\n'
    f'Ваш Индекс Массы Тела (ИМТ): {bmi:.1f}\n'
    f'Рекомендуемая норма воды: {water:.3f} л. в день\n'
    f'Расчёт окончен. Будьте здоровы!\n'
    f'{"." * SEPARATOR_WIDTH}',
)
