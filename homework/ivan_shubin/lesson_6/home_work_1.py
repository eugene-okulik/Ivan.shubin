text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

# Разделяем текст на слова
words = text.split()

# Добавляем 'ing' к каждому слову
new_words = []
for word in words:
    if word[-1] in ',.':
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
    new_words.append(new_word)

# Объединяем слова обратно в строку
new_text = ' '.join(new_words)

print(new_text)