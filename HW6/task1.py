# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


a1 = int(input('Введите первый элемент: '))
n = int(input('Введите количество элементов которые необходимо вывести: '))
d = int(input('Введите шаг арифметической прогрессии: '))
for i in range(d):
    print(a1 + i * n)
    # print(f' {d} элементов (-а) арифметической прогрессии от числа {a1} c шагом {n} = {a1 + i * d}')
