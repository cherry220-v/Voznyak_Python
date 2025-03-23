import re
test_str = open("hotline.txt", "r+", encoding="utf-8").read()
print(len(re.findall(r"Горячая линия", test_str, re.MULTILINE)))
print(test_str.replace("Горячая линия", "Горячая линия Министерства образования Ростовской области"))

last50 = re.findall(r"(.+50)(\?|$)", test_str, re.MULTILINE)
last03 = re.findall(r"(.+03)(\?|$)", test_str, re.MULTILINE)
print(len(last50))
print(len(last03))