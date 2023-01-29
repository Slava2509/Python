# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('введите трехзначное число: '))
sum_third_number = (number//100) + (number//10 % 10) + (number % 10)
print(sum_third_number)
