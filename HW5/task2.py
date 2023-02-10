# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def degree(number_a, number_b):
    if (number_a == 0):
        return number_b
    return degree(number_a-1, number_b+1)


print(degree(int(input('введите число А: ')), (int(input('введите число В: ')))))
