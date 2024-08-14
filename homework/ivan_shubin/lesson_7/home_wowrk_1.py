secret_number = 7  # Загаданное число

while True:
    guess = int(input("Угадайте цифру (от 0 до 9): "))
    if guess == secret_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова.")
