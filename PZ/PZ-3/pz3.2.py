# Спектр видимого излучения представлен в таблице. Составить программу,
# определяющую название цвета в зависимости от введенной длины волны.

wavelength = input("Введите длину волны (в нм): ")
while type(v1) != float:
    try:
        v1 = float(v1)
    except:
        wavelength = input("Введите длину волны (в нм): ")
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
