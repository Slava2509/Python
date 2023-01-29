# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5 = 9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

number_bilet = int(input('Введите номер билета '))
left_part = (number_bilet//1000)
left_sum_bilet = (left_part//100) + (left_part//10 % 10) + (left_part % 10)
print(left_sum_bilet)

right_part = ((number_bilet//1000)*1000 - number_bilet)*-1
right_sum_bilet = (right_part//100) + (right_part//10 % 10) + (right_part % 10)
print(right_sum_bilet)

if left_sum_bilet == right_sum_bilet:
    print('happy bilet')
else:
    print('not happy bilet')
