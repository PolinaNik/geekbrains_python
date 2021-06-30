"""Nikitich Polina"""

"""3. Реализовать функцию my_func(), которая принимает три позиционных 
аргумента и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    """Возвращает сумму 2-ух максимальных аргументов"""
    list_of_args = list(args)
    max_element1 = max(list_of_args)
    list_of_args.remove(max_element1)
    max_element2 = max(list_of_args)
    sum_max = max_element1 + max_element2
    return sum_max


print(my_func(100, 500, 6))
