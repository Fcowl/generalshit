import sqlite3

# Создаем соединение. Если файла 'my_database.db' нет, он создастся автоматически.
connection = sqlite3.connect('my_database.db')

# Объект cursor позволяет выполнять SQL-запросы
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Сохраняем изменения
connection.commit()