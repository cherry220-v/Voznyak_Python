# Составить генератор (yield), который выводит из строки только буквы.

def letter_generator(s):
    for i in s:
        if i.isalpha():
            yield i

s = input("Строка: ")
print("".join(letter_generator(s)))
