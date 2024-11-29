# Дан список размера N. Найти номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).

import random
def findLMax(lst):
    n = len(lst)
    if n == 1: return 0 # Единственный элемент автоматически является локальным максимумом

    lastIndex = None  # Переменная для хранения индекса последнего локального максимума
    if lst[0] > lst[1]: lastIndex = 0

    # Проверка элементов с 1 до n-2
    for i in range(1, n - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            lastIndex = i

    # Проверка последнего элемента
    if lst[-1] > lst[-2]: lastIndex = n - 1
    return lastIndex

n = input("Введите длинну случайного списка: ")
while type(n) != int:
    try:
        n = int(n)
    except:
        n = input("Введите длинну случайного списка: ")
lst = [int(random.randint(1, 100)) for i in range(n)]
lMax = findLMax(lst)
print("Список {}\nНомер последнего локального максимума: {}. Это число {}".format(lst, lMax, lst[lMax]))