import functions

# Основной цикл программы
while True:
    print("\nТелефонный справочник")
    print("1. Вывести данные")
    print("2. Добавить, сохранить данные")
    print("3. Найти")
    print("4. Изменить данные")
    print("5. Удалить данные")
    print("6. Выйти\n")

    choice = input("Выберите действие: ")
    if choice == "1":
        functions.print_data()
    elif choice == "2":
        data = input("Введите данные (Фамилия, Имя, Отчество, Номер телефона): ")
        functions.save_data(data)
    elif choice == "3":
        name = input("Введите имя или фамилию для поиска: ")
        functions.search_data(name)
    elif choice == "4":
        name = input("Введите имя или фамилию для изменения данных: ")
        functions.edit_data(name)
    elif choice == "5":
        name = input("Введите имя или фамилию для удаления данных: ")
        functions.delete_data(name)
    elif choice == "6":
        break
    else:
        print("Некорректный ввод, выберите действие")