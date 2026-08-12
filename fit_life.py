# Проект FitLife - MVP версия 1.0


# 1. Знакомство
SEPARATOR_WIDTH = 70

print('=' * SEPARATOR_WIDTH)
print('Здравствуйте! Вас приветствует программа FitLife')

user_name = input('Введите Ваше имя: ')

print(f'{user_name}, добро пожаловать!')

user_age = int(input('Сколько вам полных лет? (целое число): '))

print(
    f"{'.' * SEPARATOR_WIDTH}\n"
    f"Ваш возраст {user_age}. Приятно познакомиться, {user_name}!\n"
    f"Наша фитнес-программа поможет Вам укрепить и поддержать здоровье.\n"
    f"Нам потребуются некоторые данные о Вашем физическом состоянии."
)

# 2. Сбор данных
user_weight = float(input('Какой у вас вес (в килограммах)?: '))
user_height = float(input('Рост в метрах. Пример:"1.75". Разделить точкой: '))

# 3. Логика расчетов
ML_PER_KG = 30          # сколько миллилитров воды на 1 кг веса
ML_TO_LITERS = 1000     # сколько мл в одном литре

bmi = user_weight / (user_height ** 2)  # имт
water = (user_weight * ML_PER_KG) / ML_TO_LITERS  # вода

# 4. Вывод красивого результата
print(
    f"{'=' * SEPARATOR_WIDTH}\n"
    f"Отчёт для пользователя {user_name} (возраст: {user_age})\n"
    f"Ваш Индекс Массы Тела (ИМТ): {bmi:.1f}\n"
    f"Рекомендуемая норма воды: {water:.3f} л. в день\n"
    f"Расчёт окончен. Будьте здоровы!\n"
    f"{'.' * SEPARATOR_WIDTH}"
)

