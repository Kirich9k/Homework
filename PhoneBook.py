from os import path

file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():

    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1][0])

        return all_data


def show_all():

    if not all_data:
        print("Пустая запись")
    else:
        print(*all_data, sep="\n")


def add_new_contact():

    global last_id

    array = ['surname', 'name', 'patronymic', 'phone number']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Запись добавлена\n")
    else:
        print("Контакт уже существует")


def del_contact():

    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Введите id контакта: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Контакт удален\n")
    else:
        print("Неверные данные")


def change_contact(data_tuple):

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("Контакт уже существует")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Контакт изменен\n")


def search_contact():
    search_data = exist_contact(0, input("Введите данные для поиска: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Неверные данные")


def exist_contact(rec_id, data):

    if rec_id:
        candidates = [i for i in all_data if rec_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def data_collection(num):

    answer = input(f"Введите {num}: ")
    while True:
        if num in "surname name patronymic":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Неверные данные\n"
                       f"Используйте только буквы алфавита,"
                       f" длина номера составляет 11 цифр"
                       f"Введите {num}: ")
    return answer


def main_menu():

    play = True
    while play:
        read_records()
        answer = input("Справочник:\n"
                       "1. Показать все контакты\n"
                       "2. Добавить контакт\n"
                       "3. Поиск по контактам\n"
                       "4. Изменить контакт\n"
                       "5. Удалить контакт\n"
                       "6. Выйти\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                del_contact()
            case "6":
                play = False
            case _:
                print("Попробуйте снова\n")


def edit_menu():

    add_dict = {"1": "Фамилия", "2": "Имя", "3": "Отчество", "4": "Номер телефона"}

    show_all()
    record_id = input("Введите id контакта: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nизменить: ")
            change = input("1. Фамилия\n"
                           "2. Имя\n"
                           "3. Отчество\n"
                           "4. Номер телефона\n"
                           "5. Выйти\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("Повторите ввод")
    else:
        print("Неверные данные")

main_menu()