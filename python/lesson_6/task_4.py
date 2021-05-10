"""Nikitich Polina"""

"""4. 4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат."""


class Car:
    """базовый класс"""

    def __init__(self, speed, color, name, *args):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = args

    def go(self):
        print(f"Машина марки '{self.name}' поехала")

    def stop(self):
        print(f"Машина марки '{self.name}' остановилась")

    def turn(self, direction):
        print(f"Машина марки '{self.name}' сделала маневр {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} {self.speed}км/ч")


class TownCar(Car):
    """городская машина"""

    def __init__(self, speed, color, name, *args):
        super().__init__(speed, color, name, *args)
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            delta = self.speed - 60
            print(f"Превышение скорости автомобиля {self.name} на {delta}. Разрешенная скорость - 60 км/ч")
        else:
            print(f"Скорость автомобиля {self.name} {self.speed}км/ч")


class SportCar(Car):
    """спортивная машина"""

    def __init__(self, speed, color, name, *args):
        super().__init__(speed, color, name, *args)
        self.is_police = False


class WorkCar(Car):
    """рабочая машина"""

    def __init__(self, speed, color, name, *args):
        super().__init__(speed, color, name, *args)
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            delta = self.speed - 40
            print(f"Превышение скорости автомобиля {self.name} на {delta}. Разрешенная скорость - 40 км/ч")
        else:
            print(f"Скорость автомобиля {self.name} {self.speed}км/ч")


class PoliceCar(Car):
    """полицейская машина"""

    def __init__(self, speed, color, name, *args):
        super().__init__(speed, color, name, *args)
        self.is_police = True


undetified_car = Car(50, "gray", "Неизвестная марка")
undetified_car.show_speed()
undetified_car.go()

town_car = TownCar(100, 'red', 'Mazda')
town_car.show_speed()
town_car.turn('влево')

work_car = WorkCar(35, 'green', "Fiat")
work_car.stop()

police_car = PoliceCar(50, 'blue', 'Lada')


def check_if_police(car):
    if car.is_police:
        print(f'Машина {car.name} полицейская')
    else:
        print(f'Машина {car.name} гражданская')


check_if_police(work_car)
check_if_police(police_car)
