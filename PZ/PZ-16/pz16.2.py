# Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе.


class Animal:
    def __init__(self, species: str, age: int):
        self.species = species
        self.age = age

    def info(self):
        return f"Вид: {self.species}, Возраст: {self.age} лет"


class Dog(Animal):
    def __init__(self, age: int, breed: str):
        super().__init__("Собака", age)
        self.breed = breed

    def info(self):
        return f"{super().info()}, Порода: {self.breed}"


class Cat(Animal):
    def __init__(self, age: int, breed: str):
        super().__init__("Кошка", age)
        self.breed = breed

    def info(self):
        return f"{super().info()}, Порода: {self.breed}"

dog = Dog(age=5, breed="Лабрадор")
cat = Cat(age=3, breed="Сиамская")

print(dog.info())
print(cat.info())
