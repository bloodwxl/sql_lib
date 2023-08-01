import sqlite3

# Підключення до бази даних або створення нової, якщо вона не існує
conn = sqlite3.connect('library.db')

# Створення таблиці для зберігання інформації про книги
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  author TEXT NOT NULL,
                  genre TEXT NOT NULL
                  )''')

def add_book(title, author, genre):
    # Додавання книги до бази даних
    cursor.execute('INSERT INTO books (title, author, genre) VALUES (?, ?, ?)', (title, author, genre))
    conn.commit()
    print("Книга успішно додана до бази даних!")

def view_books():
    # Перегляд усіх книг у базі даних
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    if books:
        for book in books:
            print(f"ID: {book[0]}, Назва: {book[1]}, Автор: {book[2]}, Жанр: {book[3]}")
    else:
        print("У базі даних немає жодної книги.")

def delete_book(book_id):
    # Видалення книги з бази даних за ID
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    print("Книга успішно видалена з бази даних!")

# Приклад використання функцій:
add_book("Гаррі Поттер і філософський камінь", "Джоан Роулінг", "Фентезі")
add_book("Майстер і Маргарита", "Михайло Булгаков", "Роман")
add_book("1984", "Джордж Оруелл", "Наукова фантастика")

view_books()

delete_book(2)

view_books()

# Закриття з'єднання з базою даних
conn.close()

