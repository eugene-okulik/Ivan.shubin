def operation_controller(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)
    return wrapper


@operation_controller
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


# Пример использования:
first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))

result = calc(first, second)
print(f"Результат: {result}")
