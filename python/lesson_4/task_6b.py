"""Nikitich Polina"""

"""6. Реализовать два небольших скрипта:
Скрипт второй: итератор, повторяющий элементы некоторого списка, определенного заранее"""

from itertools import cycle

origin = ['hello', "how are you doing", 'goodbye']

c = 0
for el in cycle(origin):
    if c > 10:
        break
    print(el)
    c += 1
