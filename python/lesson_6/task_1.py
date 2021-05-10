"""Nikitich Polina"""

"""1. Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт."""

import time


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        start = time.time()
        elapsed = 1
        while elapsed < 7:
            elapsed = int(time.time() - start)
            if elapsed != 0:
                self.__color = 'red'
                time.sleep(1)
                print(self.__color)
        start = time.time()
        elapsed = 1
        while elapsed < 2:
            elapsed = int(time.time() - start)
            if elapsed != 0:
                self.__color = 'yellow'
                time.sleep(1)
                print(self.__color)
        start = time.time()
        elapsed = 1
        while elapsed < 10:
            elapsed = int(time.time() - start)
            if elapsed != 0:
                self.__color = 'green'
                time.sleep(1)
                print(self.__color)


test = TrafficLight('yellow')
test.running()
