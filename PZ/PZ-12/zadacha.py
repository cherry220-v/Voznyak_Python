import random

n = input("Введите длинну случайного списка: ")
while type(n) != int:
    try:
        n = int(n)
    except:
        n = input("Введите длинну случайного списка: ")

lst = [int(random.randint(-1, 15)) for i in range(n)]
print(list(filter(lambda x: x > 0, lst)), list(filter(lambda x: x < 0, lst)), sorted(lst)[0], sorted(lst)[-1], sum(lst)/len(lst))
# min, max
