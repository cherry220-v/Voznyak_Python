# Дано целое число N (> 0). Используя операции деления нацело и взятия остатка от
# деления, найти число, полученное при прочтении числа N справа налево.

num = input("Введите число больше 0: ")
while type(num) != int:
    try:
        num = int(num)
    except:
        num = input("Введите число больше 0: ")

if num <= 0: raise Exception("Число должно быть больше нуля") # можно сделать через if, просто так быстрее и красивее

reversedNum = 0

"""При умножении на 10 число идёт в следующий разряд, затем берётся последняя цифра числа
она переходит в новый разряд, затем последняя цифра числа уходит 
Цикл продолжается пока все разряды не перейдут в новое число
"""

while num > 0:
    reversedNum = reversedNum*10  + (num % 10)
    num //= 10

print(reversedNum)


# Я знаю про if :3
num = input("Введите число больше 0: ")
while type(num) != int:
    try:
        num = int(num)
    except:
        num = input("Введите число больше 0: ")

if num >= 0:

    reversedNum = 0

    while num > 0:
        reversedNum = reversedNum*10  + (num % 10)
        num //= 10

    print(reversedNum)
else:
    print("Число должно быть больше нуля")