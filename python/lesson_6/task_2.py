"""Nikitich Polina"""

"""2.  Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т."""


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self):
        self.weight_per_metr = 25
        self.height = 5 / 1000
        self.weight = int(self._length * self._width * self.weight_per_metr * self.height)
        print(f'Масса асфальта размерами {self._length}x{self._width} составит {self.weight} т')


route_1 = Road(5000, 20)
route_1.calculate_weight()
