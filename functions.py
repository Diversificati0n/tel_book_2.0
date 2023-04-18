# Функция для вывода данных из файла
def print_data():
    with open("book.txt", "r", encoding='utf-8') as file:
        for line in file:
            print(line.strip())

# Функция для сохранения данных в файл
def save_data(data):
    with open("book.txt", "a", encoding='utf-8') as file:
        file.write("\n" + data)

# Функция для поиска записи по имени или фамилии
def search_data(name):
    found = False
    with open("book.txt", "r", encoding='utf-8') as file:
        for line in file:
            if name.lower() in line.lower():
                print(line.strip())
                found = True
    if not found:
        print("Запись не найдена.")

# Функция для изменения данных
def edit_data(name):
    found = False
    with open("book.txt", "r+", encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if name.lower() in line.lower():
                new_data = input("Введите новые данные (Фамилия, Имя, Отчество, Номер телефона): ")
                file.write(new_data + "\n")
                found = True
            else:
                file.write(line)
        file.truncate()
    if not found:
        print("Запись не найдена.")

# Функция для удаления данных
def delete_data(name):
    found = False
    with open("book.txt", "r+", encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if name.lower() not in line.lower():
                file.write(line)
            else:
                found = True
        file.truncate()
    if not found:
        print("Запись не найдена.")
