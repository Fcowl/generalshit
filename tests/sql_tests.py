import sqlite3

# Создаем соединение. Если файла 'my_database.db' нет, он создастся автоматически.
connection = sqlite3.connect(r'C:\Users\Fcowl\Desktop\database.db')


# Объект cursor позволяет выполнять SQL-запросы
cursor = connection.cursor()
print(cursor.rowcount)
print()