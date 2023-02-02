# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y(X, Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 *

sum_xy = int(input('Первая подсказка Пети, где он назывет сумму чисел x и y: '))
multi_xy = int(
    input('Вторая подсказка, где Петя называет произведение чисел x и y: '))
first_number_x = 1
second_number_y = 1

while first_number_x < sum_xy:
    first_number_x += 1
    second_number_y = 1
    while second_number_y < sum_xy:
        second_number_y += 1
        if first_number_x + second_number_y == sum_xy and first_number_x * second_number_y == multi_xy:
            print(first_number_x, second_number_y)
