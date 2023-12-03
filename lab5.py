class Person:
    def __init__(self, full_name: str):
        self.full_name = full_name


class Driver(Person):

    def __init__(self, experience: int, full_name: str):
        super().__init__(full_name)
        self.experience = experience


class Engine:

    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company


class Car:

    def __init__(self, car_class: str, engine: Engine, driver: Driver, weight: int, brand: str):
        self.car_class = car_class
        self.engine = engine
        self.driver = driver
        self.brand = brand
        self.weight = weight

    def start(self) -> None:
        print('Поехали')

    def stop(self) -> None:
        print('Останавливаемся')

    def turn_right(self) -> None:
        print('Поворот направо')

    def turn_left(self) -> None:
        print('Поворот налево')

    def __str__(self):
        return f"Марка: {self.brand}, Класс: {self.car_class}, Вес: {self.weight} kg\n" \
               f"Водитель: {self.driver.full_name}, Стаж вождения: {self.driver.experience} лет\n" \
               f"Мотор: {self.engine.power} л.с, {self.engine.company}"


class Lorry(Car):
    def __init__(self, carrying: int, car_class: str, engine: Engine, driver: Driver, weight: int,
                 brand: str):
        super().__init__(car_class, engine, driver, weight, brand)
        self.carrying = carrying

    def __str__(self):
        return f"Марка: {self.brand}, Класс: {self.car_class}, Вес: {self.weight} kg\n" \
               f"Водитель: {self.driver.full_name}, Стаж вождения: {self.driver.experience} лет\n" \
               f"Мотор: {self.engine.power} л.с, {self.engine.company}"


class SportCar(Car):
    def __init__(self, speed: float, car_class: str, engine: Engine, driver: Driver, weight: int, brand: str):
        super().__init__(car_class, engine, driver, weight, brand)
        self.speed = speed

    def __str__(self):
        return f"Марка: {self.brand}, Класс: {self.car_class}, Вес: {self.weight} kg\n" \
               f"Водитель: {self.driver.full_name}, Стаж вождения: {self.driver.experience} лет\n" \
               f"Мотор: {self.engine.power} л.с, {self.engine.company}"


driver1 = Driver(5, 'Иван Иванов')
engine1 = Engine(200, "Toyota")
car1 = Car('Седан', engine1, driver1, 1500, 'Toyota Camry')

lorry1 = Lorry(5000, 'Грузовик', engine1, driver1, 1500, 'Mercedes-Benz Actros')
sportcar1 = SportCar(330, 'Спорткар', engine1, driver1, 1500, 'Ferrari 488 GTB')

print(car1)
print(lorry1)
print(sportcar1)
