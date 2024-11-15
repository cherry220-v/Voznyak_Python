import random
def reverseBetweenMinMax(lst):
    if len(lst) < 2:  # Если список слишком короткий (1 или 0 элементов), возвращаем его как есть
        return lst
    
    # Находим индексы минимального и максимального элементов и упорядочиваем их
    start, end = sorted((lst.index(min(lst)), lst.index(max(lst))))
    
    # Разворачиваем подсписок между минимальным и максимальным элементами (включительно)
    lst[start:end + 1] = lst[start:end + 1][::-1]
    return lst

n = int(input("Введите длинну случайного списка: "))
lst = [int(random.randint(1, 100)) for i in range(n)]
print("Исходный список:", lst)
print("Результат:", reverseBetweenMinMax(lst))
