# Создаем словарь my_dict


my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {100, 200, 300, 400, 500}
}

# Для ключа 'tuple': вывести на экран последний элемент


print("Последний элемент в 'tuple':", my_dict['tuple'][-1])

# Для ключа 'list': добавить элемент и удалить второй элемент


my_dict['list'].append(60)
del my_dict['list'][1]

# Для ключа 'dict': добавить элемент и удалить один элемент


my_dict['dict'][('i am a tuple',)] = 'new value'
del my_dict['dict']['a']

# Для ключа 'set': добавить новый элемент и удалить элемент из множества


my_dict['set'].add(600)
my_dict['set'].remove(100)

# Выводим итоговый словарь на экран


print("Итоговый словарь:", my_dict)

# Создаем словарь my_dict


my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {100, 200, 300, 400, 500}
}

# Для ключа 'tuple': вывести на экран последний элемент


print("Последний элемент в 'tuple':", my_dict['tuple'][-1])

# Для ключа 'list': добавить элемент и удалить второй элемент


my_dict['list'].append(60)
del my_dict['list'][1]

# Для ключа 'dict': добавить элемент и удалить один элемент


my_dict['dict'][('i am a tuple',)] = 'new value'
del my_dict['dict']['a']

# Для ключа 'set': добавить новый элемент и удалить элемент из множества


my_dict['set'].add(600)
my_dict['set'].remove(100)

# Выводим итоговый словарь на экран


print("Итоговый словарь:", my_dict)
