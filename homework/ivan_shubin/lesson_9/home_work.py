from datetime import datetime

# --- Обработка даты ---
# Дана дата
date_str = "Jan 15, 2023 - 12:05:33"

# Преобразование строки в объект datetime
date_obj = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

# 1. Полное название месяца
month_name = date_obj.strftime("%B")
print("Полное название месяца:", month_name)

# 2. Дата в формате "15.01.2023, 12:05"
formatted_date = date_obj.strftime("%d.%m.%Y, %H:%M")
print("Дата в формате '15.01.2023, 12:05':", formatted_date)

# --- Работа со списком температур ---
# Данный список температур
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

# Список жарких дней (выше 28 градусов)
hot_days = list(filter(lambda x: x > 28, temperatures))

# Расчет максимальной, минимальной и средней температуры
max_temp = max(hot_days)
min_temp = min(hot_days)
avg_temp = sum(hot_days) / len(hot_days)

# Вывод результатов
print("Жаркие дни:", hot_days)
print("Максимальная температура:", max_temp)
print("Минимальная температура:", min_temp)
print("Средняя температура:", round(avg_temp, 2))

