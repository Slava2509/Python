# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2
# *
from random import randint

monets = int(input('Введите какое количество монет лежит на столе: '))
eagle_monets = 0
tails_monets = 0
order_of_coins = 0

for i in range(1, monets + 1):
    order_of_coins = randint(0, 1)
    print(order_of_coins)

    if order_of_coins > 0:
        tails_monets = tails_monets + 1
    else:
        eagle_monets = eagle_monets + 1

print(
    f'монет лежащих орлом вверх {eagle_monets}, монет лежащих решкой вверх {tails_monets}')
if eagle_monets > tails_monets:
    print(
        f'Проще перевернуть монет лежащих решкой вверх в количестве: {tails_monets} шт')
elif eagle_monets == tails_monets:
    print(
        f'все равно что переворачивать')
else:
    print(
        f'Проще перевернуть монет лежащих орлом вверх в количестве: {eagle_monets} шт')
