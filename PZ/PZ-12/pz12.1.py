# В последовательности на n целых чисел умножить элементы до n-1 на элемент n.
import random
def multiply_by_last(seq):
    if not seq:
        return []
    last = seq[-1]
    return list(map(lambda x: x * last, seq[:-1])) + [last]

n = input("Введите длинну случайного списка: ")
while type(n) != int:
    try:
        n = int(n)
    except:
        n = input("Введите длинну случайного списка: ")

lst = [int(random.randint(1, 100)) for i in range(n)]
print(multiply_by_last(lst))
