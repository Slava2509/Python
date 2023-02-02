# Требуется вывести все целые степени двойки(т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input('Введите любое число: '))
degree = 1
print(degree)

while 2*degree < number:
    print(2*degree)
    degree *= 2
