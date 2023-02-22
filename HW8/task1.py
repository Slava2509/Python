# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def append_list(n: str, f: str, t: str) -> list:
    list = []
    list.append(n)
    list.append(f)
    list.append(t)
    return list


def list_to_str(list: list) -> str:
    return list[0] + ' ' + list[1] + ' ' + list[2] + '\n'


flag = True
while flag:
    print('1. Открыть файл')
    print('2. Сохранить файл')
    print('3. Показать контакты')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Найти контакт')
    print('7. Удалить контакт')
    print('8 Выход')
    punkt = int(input('Введите пункт меню:'))
    match punkt:
        case 1:
            data = open('file.txt', 'a')
        case 2:
            data.close()
        case 3:
            data = open('file.txt', 'r')
            for line in data:
                print(line)

        case 4:
            list_abon = []
            name_a = input('Введите имя: ')
            name_f = input('Введите фамилию: ')
            tel_no = input('Введите номер: ')
            list_abon = append_list(name_a, name_f, tel_no)
            str_abon = str(list_abon[0]) + ' ' + \
                str(list_abon[1]) + ' ' + str(list_abon[2]) + '\n'
            data.writelines(str_abon)
        case 5:
            print(ggg)
            list_find = []
            data = open('file.txt', 'r')
            for line in data:
                list_find.append(line.split())
            print(list_find)
            find_str = input('Введите контакт для изменения (тел.): ')
            name_a = input('Введите имя:')
            name_f = input('Введите фамилию:')

            for item in list_find:
                if item[2] == str(find_str):
                    item[0] = name_a
                    item[1] = name_f
            data = open('file.txt', 'w+')
            for item in list_find:
                data.writelines(list_to_str(item))
            data.close()
        case 6:
            find_str = input(
                'Введите тел.номер контакта которого необходимо найти: ')
            list_find = []
            data = open('file.txt', 'r')
            for line in data:
                list_find.append(line.split())
            print(list_find)
            for item in list_find:
                if item[2] == find_str:
                    print(item)
        case 7:
            find_str = input(
                'Введите тел.номер контакта который необходимо удалить: ')
            list_find = []
            data = open('file.txt', 'r')
            for line in data:
                list_find.append(line.split())
            print(list_find)
            for item in list_find:
                if item[2] == find_str:
                    list_find.remove(item)
            data = open('file.txt', 'w+')
            for item in list_find:
                data.writelines(list_to_str(item))
            data.close()

        case 8:
            flag = False
