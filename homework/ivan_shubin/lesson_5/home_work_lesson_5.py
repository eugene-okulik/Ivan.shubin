# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(f"Name: {name}, Last Name: {last_name}, City: {city}, Phone: {phone}, Country: {country}")

# Задание 2
results = [
    'результат операции: 42',
    'результат операции: 514',
    'результат работы программы: 9'
]
for result in results:
    index = result.index(':') + 2
    number = int(result[index:])
    print(number + 10)

# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students_text = ', '.join(students)
subjects_text = ', '.join(subjects)
print(f"Students {students_text} study these subjects: {subjects_text}")
