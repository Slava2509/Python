# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да

word = input('Введите фразы Винни-Пуха через пробел: ').upper()
string = word.split()
print(string)
def rifma(x): return sum(1 for i in x if i in 'А')


rifma_word = (rifma(string[0]))
if all([rifma(i) == rifma_word for i in string]):
    print('Парам пам-пам')
else:
    print('Пам парам')
