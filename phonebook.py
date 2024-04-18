from io import*
import os

# Добавление в файл phonebook.txt данные в словаре из creating_contact
def add_new_contact(contact):
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(value)
            file.write(';')
        file.write('\n')
    return True


def creating_contact():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    comment = input('Примечание (необязательно): ')
    contact = {
        'second_name': second_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number,
        'comment': comment
        }
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print(f"\nПроверьте данные\nФамилия: {second_name}\nИмя: {first_name}\nОтчество: {middle_name}\nНомер телефона: {phone_number}\nКоментарий: {comment}\nЕсли данные введены корректно нажмите д. Если нет - н\n> ")
        sel = input()
        if sel == 'д':
            add_new_contact(contact)
            print(f"Контакт {second_name} {first_name} {middle_name} успешно создан!")
            input('Нажмите ENTER, чтобы продолжить')
            main_menu()
        elif sel == 'н':
            creating_contact()
        else:
            print('Пожалуйста, введите Д или Н')

def open_phonebook():
    try:
        with open('phonebook.txt', 'r', encoding='utf-8') as file:
            pass
    except FileNotFoundError:
        print("Ошибка. Файла не существует.")
    else:
        title = ["Фамилия", "Имя", "Отчество", "Телефон", "Описание"]
        with open('phonebook.txt', 'r', encoding='utf8') as file:
            print("\t\t".join(title))
            for line in file:
                print("\t\t".join(line.split(";")))
    input("Нажмите ENTER для продолжения")
    main_menu()
# Экспорт найденного (выбранного) контакта пользователем
def export_contact(contact_num):  
        with open('phonebook.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            with open('tempbook.txt', 'w', encoding='utf-8') as file:
                file.write(lines[contact_num])
                print("Запись экспортирована успешно!")
                input('Нажмите ENTER, чтобы продолжить')
# "Меню" опций для взаимодействия с найденым (выбранным) контактом
def option(contact_num):
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f'Выбран контакт:\n{" ".join(lines[contact_num].split(";"))}')
    while True:
        var = int(input('Что сделать с выбранным контактом?\n1 -- Экспорт контакта\n2 -- Удалить контакт\n3 -- вернуться\n4 -- выйти в главное меню\n> '))
        if var == 1:
            export_contact(contact_num)
        elif var == 2:
            del_contact(contact_num)
        elif var == 3:
            find_method()
        elif var == 4:
            main_menu()
        else:
            print("Неверный выбор")
# удаление найденного (выбранного) контакта
def del_contact(contact_num):
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f'Вы удаляете следующую запись:\n{" ".join(lines[contact_num].split(";"))}')
        choice =  input("Продолжить?\nд -- да, удалить\nн -- отмена\n> ")
        while True:
            if choice == "д":
                with open('phonebook.txt', 'w', encoding='utf-8') as file:
                    file.write(''.join(lines[:contact_num] + lines[contact_num + 1:]))
                    print("Запись успешно удалена")
                    input('Нажмите ENTER, чтобы выйти в меню')
                    main_menu()
            elif choice == "н":
                find_method()
            else:
                print("Пожалуйста, подвердите или отмените выбор")
# варианты поиска контакта
def find_method():
    while True:
        try:
            method = int(input("Найти контакт по:\n1 -- фамилии\n2 -- имени\n3 -- отчеству\n4 -- номеру\n0 -- <НАЗАД\n> "))
        except ValueError:
            print("Введено неверное значение. Повторите попытку.")
        else:
            if 4 >= method != 0:
                method -= 1
                text = input('Введите данные для поиска: ')
                search(text, method)
            elif method == 0:
                main_menu()
            else:
                print("Неверный выбор!")

def search(search_phrase, search_method):
    print(search_method)
    title = ["№", "Фамилия", "Имя", "Отчество", "Телефон"]
    # status необходим, для дальнешей обработки найденных контактов. если найденный контакт уникальный, то выбор найденного контакта отпадает
    status = 0
    # num - служит в роле ID каждой строки
    num = 0
    # found_num_range в дальнейшем добавляет в себя ID найденых контактов. Служит для доп проверки, если в дальнейшем пользователь выбрал контакт не из списка. 
    found_num_range = []
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("Результаты поиска:\n")
        print("\t\t".join(title))
        for counter,line in enumerate(file):
            line = line.split(";")
            if search_phrase in line[search_method]:
                status += 1
                found_num_range.append(counter)
                print(counter,"\t\t", "\t\t".join(line))
                num = counter
        if status == 0:
            print('Контактов не найдено')
            input('Нажмите ENTER, чтобы повторить')
            find_method()
        if status > 1:
            num = int(input("Выберите контакт по его №\n> "))
            checking_for_range = False
            while checking_for_range == False:
                for i in found_num_range:
                    if i == num:
                        option(num)
                else:
                    print("Выбранный контакт НЕ в диапазоне")
                    input('Нажмите ENTER, чтобы повторить')
                    find_method()
        elif status == 1:
            input('Нажмите ENTER, чтобы продолжить')
            option(num)

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Главное меню телефонной книги.\nВыберите необходимую опцию")
        print("1. Создать новый контакт.","2. Удалить контакт","3. Поиск записи","4. Просмотреть все записи","0. ВЫХОД", sep="\n")
        try:
            select = int(input("Выберите пункт и нажмите Ether:\n> "))
        except ValueError:
            print("Пожалуйста, введите корректный пункт!\n")
        else:
            if select == 1:
                creating_contact()
            elif select == 2:
                find_method()
            elif select == 3:
                find_method()
            elif select == 4:
                open_phonebook()
            elif select == 0:
                break
            else:
                print("Пожалуйста, введите корректный пункт!\n")
             
main_menu()