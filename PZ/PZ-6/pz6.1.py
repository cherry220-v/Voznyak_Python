a = int(input("Введите стартовое число для последовательности: "))
d = int(input("Введите знаменатель последовательности: "))
print([a*d**(i) for i in range(10)])