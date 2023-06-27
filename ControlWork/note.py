# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат(разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента

# from datetime import datetime


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
    print('1. Открыть заметки')
    print('2. Сохранить заметку')
    print('3. Показать заметки')
    print('4. Добавить заметку')
    print('5. Изменить заметку')
    print('6. Найти заметку')
    print('7. Удалить заметку')
    print('8 Выход')
    punkt = int(input('Введите пункт меню:'))
    match punkt:
        case 1:
            data = open('note.json', 'a')
        case 2:
            data.close()
        case 3:
            data = open('note.json', 'r')
            for line in data:
                print(line)

        case 4:
            list_note = []
            id_a = input('Введите идентификатор: ')
            heading_f = input('Введите заголовок: ')
            note_no = input('Введите заметку: ')
            # date_d = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            list_note = append_list(id_a, heading_f, note_no)
            # + date_d
            str_note = str(list_note[0]) + ' ' + \
                str(list_note[1]) + ' ' + str(list_note[2]) + '\n'
            data.writelines(str_note)
        case 5:
            print()
            list_find = []
            data = open('note.json', 'r')
            for line in data:
                list_find.append(line.split())
            print(list_find)
            find_str = input('Введите заметку для изменения: ')
            heading_f = input('Введите заголовок: ')
            note_no = input('Введите заметку: ')

            for item in list_find:
                if item[2] == str(find_str):
                    item[0] = heading_f
                    item[1] = note_no
            data = open('note.json', 'w+')
            for item in list_find:
                data.writelines(list_to_str(item))
            data.close()
        case 6:
            find_str = input(
                'Введите заметку которую необходимо найти: ')
            list_find = []
            data = open('note.json', 'r')
            for line in data:
                list_find.append(line.split())
            print(list_find)
            for item in list_find:
                if item[1] == find_str:
                    print(item)
        case 7:
            find_str = input(
                'Введите заметку которую необходимо удалить: ')
            list_find = []
            data = open('note.json', 'r')
            for line in data:
                list_find.append(line.split())
            print(list_find)
            for item in list_find:
                if item[1] == find_str:
                    list_find.remove(item)
            data = open('note.json', 'w+')
            for item in list_find:
                data.writelines(list_to_str(item))
            data.close()

        case 8:
            flag = False
