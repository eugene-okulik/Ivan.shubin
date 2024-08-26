def finish_me(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)  # Выполнение исходной функции
        print("finished")  # Печать "finished" после выполнения функции
    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
