# Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы
# неравенства A > 2 и B < 3».

A = input("Введите целое число A: ")
while type(A) != int:
    try:
        A = int(A)
    except:
        A = input("Введите целое число A: ")

B = input("Введите целое число B: ")
while type(B) != int:
    try:
        B = int(B)
    except:
        B = input("Введите целое число B: ")

# Проверка и вывод результата
if A > 2 and B < 3:
    print("Истинно: A > 2 и B < 3")
else:
    print("Ложно: A > 2 и B < 3")