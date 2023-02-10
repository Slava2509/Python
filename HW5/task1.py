# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.


def degree(number_a, number_b):
    if (number_b == 1):
        return (number_a)
    return number_a*degree(number_a, number_b-1)


print(degree(int(input('введите число А: ')), (int(input('введите число В: ')))))
