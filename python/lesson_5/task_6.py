"""Nikitich Polina"""

"""6. Сформировать (не программно) текстовый файл. 
В нём каждая строка должна описывать учебный предмет 
и наличие лекционных, практических и лабораторных занятий 
по предмету. Сюда должно входить и количество занятий. 
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее 
количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re

subject_file = open('text_6.txt', 'r', encoding='utf-8')

subject = subject_file.readlines()

subject_dict = {}

pat = re.compile(r'[0-9]+')  # паттерн для нахождения всех цифр в строке

for string in subject:
    list_of_items = string.split(" ")
    name_of_subject = list_of_items[0][:-1]  # название предмета без двоеточия (:)
    search1 = pat.search(list_of_items[1])
    search2 = pat.search(list_of_items[2])
    search3 = pat.search(list_of_items[3])
    hours = []
    if search1:
        hours.append(int(search1.group()))
    if search2:
        hours.append(int(search2.group()))
    if search3:
        hours.append(int(search3.group()))
    sum_of_hours = sum(hours)
    value_for_dict = {name_of_subject: sum_of_hours}
    subject_dict.update(value_for_dict)

print(subject_dict)
