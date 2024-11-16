# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.

cost = input("Введите цену за 1 кг конфет: ")
while type(cost) != int:
    try:
        cost = int(cost)
    except:
        cost = input("Введите цену за 1 кг конфет: ")

for i in range(10):
    print("Цена за {} = {}".format((i+1)*0.1, (i+1)*0.1*cost))
    