import random

# Запрашиваем у пользователя зарплату
salary = int(input("Введите вашу зарплату: "))

# Генерируем случайное значение для бонуса (True или False)
bonus = random.choice([True, False])

# Если бонус есть, добавляем случайное число от 1 до 5000 к зарплате
if bonus:
    salary += random.randint(1, 5000)

# Выводим результат
print(f'{salary}, {bonus} - ${salary}')
