"""Nikitich Polina"""

""" 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта 
заработной платы сотрудника. 
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время 
выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

script_name, hours, salary_per_hour, bonus = argv


def calculate_salary():
    salary = (int(hours) * int(salary_per_hour)) + int(bonus)
    return f"the salary of worker is {salary} rubles"


print(calculate_salary())

