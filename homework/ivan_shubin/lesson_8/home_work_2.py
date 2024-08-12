def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Создаем генератор
fib_gen = fibonacci_generator()

# Получаем нужные числа
for i in range(1, 100001):
    fib_num = next(fib_gen)
    if i in [5, 200, 1000, 100000]:
        print(f'{i}-е число Фибоначчи: {fib_num}')
