# В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
# фразу «Министерства образования Ростовской области», посчитать количество
# произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
# «50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re

with open("hotline.txt", "r+", encoding="utf-8") as file:
    text = file.read()

text, count_replacements = re.subn(r"Горячая линия", "Горячая линия Министерства образования Ростовской области", text)

last50 = re.findall(r"[0-9]+50", text)
last03 = re.findall(r"[0-9]+03", text)
 
ege_gia_numbers = re.findall(r"\d{7,}", "\n".join(re.findall(r".*ЕГЭ.*|.*ГИА.*", text)))

print("Количество замен:", count_replacements)
print("Количество номеров на 50:", len(last50))
print("Количество номеров на 03:", len(last03))
print("Номера горячих линий по ЕГЭ/ГИА:", ", ".join(ege_gia_numbers))

with open("hotline2.txt", "w", encoding="utf-8") as file:
    file.write(text)
