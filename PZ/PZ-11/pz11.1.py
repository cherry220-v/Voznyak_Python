import random
l = [" ".join([str(int(random.randint(-100, 100))) for i in range(10)])] # генерируем список случайных чисел
f3 = open('data.txt', 'w')
f3.writelines(l)
f3.close()
# Дублируем список в новый файл data_4.txt
f4 = open('data2.txt', 'w', encoding="utf-8")
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()
# разбиваем строку и ее значения преобразуем в числа
f3 = open('data.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

f3 = open('data.txt')

# Так как список начинается, то первый элемент будет первым максимальным элементом (Его не с чем сравнивать)

f4 = open('data2.txt', 'a', encoding="utf-8")
f4.write('\n')
print(f'Количество элементов: {len(k)}', f'Минимальный элемент: {min(k)}', f"Элементы умноженные на первый максимальный элемент ({k[0]}): {[i*k[0] for i in k]}", sep="\n", file=f4)
f4.close()