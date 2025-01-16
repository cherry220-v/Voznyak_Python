# Дан список размера N. Переставить в обратном порядке элементы список,
# расположенные между его минимальным и максимальным элементами, включая
# минимальный и максимальный элементы.

import random
def reverseBetweenMinMax(lst):
    if len(lst) < 2:  # Если список слишком короткий (1 или 0 элементов), возвращаем его как есть
        return lst

    # Находим индексы минимального и максимального элементов и упорядочиваем их
    start, end = lst.index(min(lst)), lst.index(max(lst))

    # Разворачиваем подсписок между минимальным и максимальным элементами (включительно)
    print(lst[start:end + 1])
    print(lst[start:end + 1][::-1])
    lst[start:end + 1] = lst[start:end + 1][::-1]
    return lst

n = input("Введите длинну случайного списка: ")
while type(n) != int:
    try:
        n = int(n)
    except:
        n = input("Введите длинну случайного списка: ")

lst = [int(random.randint(1, 100)) for i in range(n)]
print("Исходный список:", lst)
print("Результат:", reverseBetweenMinMax(lst))
