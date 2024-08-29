class Book:
    # Общие атрибуты для всех книг
    material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        # Индивидуальные атрибуты для каждой книги
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        # Формирование строки с деталями книги
        if self.reserved:
            return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, "
                    f"материал: {self.material}, зарезервирована")
        else:
            return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, "
                    f"материал: {self.material}")


# Создание экземпляров книг
book1 = Book("Идиот", "Достоевский", 500, "978-5-17-082650-4")
book2 = Book("Мастер и Маргарита", "Булгаков", 400, "978-5-17-111163-9")
book3 = Book("Война и мир", "Толстой", 1200, "978-5-17-074547-6")
book4 = Book("Преступление и наказание", "Достоевский", 600, "978-5-17-102402-0")
book5 = Book("Анна Каренина", "Толстой", 900, "978-5-389-08969-3")

# Резервирование одной книги
book3.reserved = True

# Вывод информации о книгах
books = [book1, book2, book3, book4, book5]
for book in books:
    print(book)


class Textbook(Book):
    def __init__(self, title, author, pages, isbn, subject, grade, has_assignments, reserved=False):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject  # Предмет
        self.grade = grade  # Класс (школьный)
        self.has_assignments = has_assignments  # Наличие заданий

    def __str__(self):
        # Формирование строки с деталями учебника
        base_info = (f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, "
                     f"предмет: {self.subject}, класс: {self.grade}")
        if self.reserved:
            return base_info + ", зарезервирована"
        else:
            return base_info


# Создание экземпляров учебников
textbook1 = Textbook("Алгебра", "Иванов", 200, "978-5-123-45678-9", "Математика", 9, True)
textbook2 = Textbook("История России", "Петров", 300, "978-5-234-56789-0", "История", 10, False)
textbook3 = Textbook("Физика", "Сидоров", 250, "978-5-345-67890-1", "Физика", 11, True)

# Резервирование одного учебника
textbook2.reserved = True

# Вывод информации об учебниках
textbooks = [textbook1, textbook2, textbook3]
for textbook in textbooks:
    print(textbook)
