def getUppercaseLetters(n):
    if not (1 < n < 26):  # Проверяем, что n находится в допустимом диапазоне
        return "n должно быть в диапазоне от 2 до 25"
    return "".join(chr(65 + i) for i in range(n))

# 65 это код буквы A в ascii. Далее все буквы идут по порядку

n = input("Введите число n (1 < n < 26): ")
while type(n) != int:
    try:
        n = int(n)
        if 1 < n < 26:
            continue
        else:
            n = input("Введите число n (1 < n < 26): ")
    except:
        n = input("Введите число n (1 < n < 26): ")
print(getUppercaseLetters(n))

# Получение из модуля strings

import string
print(string.ascii_letters[:n].upper())

# Ну и ручками

ascii_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(ascii_letters[:n])