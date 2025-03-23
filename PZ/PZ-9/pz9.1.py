# Дан словарь с четным количеством элементов. Найти суммы значений
# элементов первой и второй половин с использованием функции. Результаты вывести
# на экран.

def sumHalves(d):
    values = list(d.values())
    half = len(values) // 2
    sumFirstHalf = sum(values[:half])
    sumSecondHalf = sum(values[half:])
    return sumFirstHalf, sumSecondHalf

def sumHalves(d): return sum(list(d.values())[:len(list(d.values())) // 2]), sum(list(d.values())[len(list(d.values())) // 2:])

import string, random
d = dict()
for i in range(10):
    d[string.ascii_letters[i]] = random.randint(1, 100)
if not (len(d) % 2):
    print("Словарь: {}".format(d))
    firstHalf, secondHalf = sumHalves(d)
    print(f"Сумма первой половины: {firstHalf}")
    print(f"Сумма второй половины: {secondHalf}")
else:
    print("Длинна словаря должна быть чётной")