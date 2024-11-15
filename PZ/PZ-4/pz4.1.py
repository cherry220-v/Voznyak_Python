cost = int(input("Введите цену за 1 кг конфет: "))
for i in range(10):
    print("Цена за {} = {}".format(i*0.1, i*0.1*cost))
    