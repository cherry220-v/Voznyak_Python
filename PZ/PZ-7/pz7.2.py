# Дана строка-предложение. Зашифровать ее, поместив вначале все символы,
# расположенные на четных позициях строки, а затем, в обратном порядке, все
# символы, расположенные на нечетных позициях (например, строка «Программа»
# превратится в «ргамамроП»).

line = input("Введите строку которую надо закодировать: ")
print(str(line[::2]+line[1::2][::-1])[::-1])