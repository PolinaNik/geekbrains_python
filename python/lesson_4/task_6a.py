"""Nikitich Polina"""

"""6. Реализовать два небольших скрипта:
Скрипт первый: итератор, генерирующий целые числа, начиная с указанного"""

from sys import argv
from itertools import count

script_name, first_number = argv

for el in count(int(first_number)):
    if el > 50:
        break
    else:
        print(el)
