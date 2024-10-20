# Ввод длины волны
wavelength = float(input("Введите длину волны (в нм): "))

# Определение цвета
if wavelength < 450:
    color = "Фиолетовый"
elif 450 <= wavelength < 480:
    color = "Синий"
elif 480 <= wavelength < 510:
    color = "Сине-зелёный"
elif 510 <= wavelength < 550:
    color = "Зелёный"
elif 550 <= wavelength < 570:
    color = "Жёлто-зелёный"
elif 570 <= wavelength < 590:
    color = "Желтый"
elif 590 <= wavelength < 630:
    color = "Оранжевый"
else:  # wavelength >= 630
    color = "Красный"

# Вывод результата
print(f"Цвет с длиной волны {wavelength} нм: {color}")
