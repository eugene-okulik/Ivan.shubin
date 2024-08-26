def repeat_me(func):
    def wrapper(*args, count=1, **kwargs):
        for _ in range(count):
            func(*args, **kwargs)  # Повторяем выполнение функции указанное число раз
    return wrapper

@repeat_me
def example(text):
    print(text)

example('print me', count=2)
