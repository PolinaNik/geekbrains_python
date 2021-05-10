"""Nikitich Polina"""

"""3. Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = sum(income.values())


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход работника с учетом премии {self._income}')


worker = Position("Николай", "Александров", "Технический директор", {"wage": 125000, "bonus": 50000})
worker.get_full_name()
worker.get_total_income()
