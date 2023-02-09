# Даны два неупорядоченных набора целых чисел(может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from random import randint

numbers_1 = int(input('Введите число для первого набора чисел: '))
numbers_2 = int(input('Введите число для второго набора чисел: '))
print(numbers_1, numbers_2)

list_1 = []
for i in range(numbers_1):
    list_1.append(randint(1, 20))

list_2 = []
for i in range(numbers_2):
    list_2.append(randint(1, 20))

print(list_1)
print(list_2)

list1 = set(list_1)
list2 = set(list_2)

i = list1.intersection(list2)
print(i)
