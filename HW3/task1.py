# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint

my_list = []
for _ in range(20):
    my_list.append(randint(0, 100))
print(my_list)
search_x = int(input('Введите искомое число от 0 до 100: '))
count = 0
nearest = 0
near = []

if search_x > 100:
    print('Введено не корректное значение числа, которое в списке отсутствует')

for i in my_list:
    if search_x == i:
        count += 1
    elif abs(search_x-i) < abs(search_x-nearest) or abs(search_x-i) < abs(search_x-nearest):
        nearest = i

near.append(nearest)

if count > 0:
    print(f'Число {search_x} встречается в заданном списке {count} раз(а)')
else:
    print(
        f'Cамое минимально близкое значение {search_x} в списке является: {near}')
