def calcDistance(v1, v2, initialDistance=8):
    return initialDistance + (v1 + v2)

v1 = float(input("Введите скорость первого автомобиля (км/ч): "))
v2 = float(input("Введите скорость второго автомобиля (км/ч): "))

newDistance = calcDistance(v1, v2)

print(f"Расстояние между автомобилями через 1 час: {newDistance} км")

# Если функции нельзя, то есть вариант попроще

print(f"Расстояние между автомобилями через 1 час: {8+float(input('Введите скорость первого автомобиля (км/ч): '))+float(input('Введите скорость второго автомобиля (км/ч): '))} км")
