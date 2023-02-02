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
#     if first_number_x+second_number_y == sum_xy:
#         temp_sum1 = (first_number_x, second_number_y)
#     while second_number_y < sum_xy:
#         second_number_y += 1
#         if first_number_x+second_number_y == sum_xy:
#             temp_sum1 = (first_number_x, second_number_y)
#         if first_number_x + second_number_y == sum_xy and first_number_x * second_number_y == multi_xy:
#             print(first_number_x, second_number_y)


# while first_number_x < sum_xy:
#     first_number_x += 1
#     if first_number_x+second_number_y == sum_xy:
#         temp_sum1 = (first_number_x, second_number_y)
#     while second_number_y < sum_xy:
#         second_number_y += 1
#         if first_number_x+second_number_y == sum_xy:
#             temp_sum1 = (first_number_x, second_number_y)
#         if first_number_x + second_number_y == sum_xy and first_number_x * second_number_y == multi_xy:
#             print(first_number_x, second_number_y)


# while first_number_x+second_number_y <= sum_xy:
#     first_number_x += 1
#     second_number_y += 1
#     # (first_number_x+1)+second_number_y and (first_number_x)+(second_number_y+1)
#     if first_number_x + second_number_y == sum_xy and first_number_x * second_number_y == multi_xy:
#         print(first_number_x, second_number_y)


# for i in range(first_number_x+second_number_y=first_number_x):
#     temp = 0
#     :

# sum_xy = int(input('Первая подсказка Пети, где он назывет сумму чисел x и y: '))
# multi_xy = int(
#     input('Вторая подсказка Пети, где он называет произведение чисел x и y: '))
# first_number_x = 0
# second_number_y = 0
# while first_number_x <= 1000:
#     while second_number_y == sum_xy - first_number_x:
#         if sum_xy == first_number_x + second_number_y and multi_xy == first_number_x*second_number_y:
#             print(first_number_x, second_number_y)

# read(s, p)
# for x = 1..1000{
#     for y = x..1000{
#         if (x+y == s и x*y == p) write(x, ' ', y)
#     }
# }

# a, b = map(int, input().split())
# c = 0
# for i in range(a + b):
#     if c:
#         break
#     for j in range(a + b):
#         if i + j == a and i * j == b:
#             c = 1
#             print(*sorted([i, j]))
#             break

# sum_xy = int(input('Первая подсказка Пети, где он назывет сумму чисел x и y: '))
# multi_xy = int(input('Вторая подсказка Пети, где он называет произведение чисел x и y: '))
# first_number_x = sum_xy - second_number_y
# while first_number_x <= 1000:
#     second_number_y = sum_xy - first_number
#     if ((first_number_x <= second_number_y and first_number*second_number_y) == multi_xy):
#         print(first_number_x, second_number_y)

# for x = 1..30000{
#     y = s-x;
#     if (x <= y и x*y == p)
