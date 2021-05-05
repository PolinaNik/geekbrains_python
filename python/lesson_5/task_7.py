"""Nikitich Polina"""

"""7. Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка будет содержать данные о фирме: название, 
форма собственности, выручка, издержки. 
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. Если фирма получила убытки, в расчёт средней 
прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. Если фирма получила убытки, 
также добавить её в словарь (со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

list_of_firms = []

with open('text_7.txt', 'r', encoding='utf-8') as firm_file:
    firms = firm_file.readlines()
    for item in firms:
        list_of_firms.append(item)

profit_firms = {}
damages_firms = {}

for string in list_of_firms:
    string_list = string.split(" ")
    name_firm = string_list[0]
    earnings = int(string_list[2])
    costs = int(string_list[3])
    if earnings > costs:
        profit = earnings - costs
        value_for_dict = {name_firm: profit}
        profit_firms.update(value_for_dict)
    else:
        damages = abs(earnings - costs)
        value_for_dict = {name_firm: damages}
        damages_firms.update(value_for_dict)

average_profit = sum(profit_firms.values()) / len(profit_firms.values())
average_damages = sum(damages_firms.values()) / len(damages_firms.values())

profit_dict = {"average_profit": int(average_profit)}
damages_dict = {"average_damages": int(average_damages)}

with open('json_file_7.json', 'w') as json_file:
    json.dump([profit_firms, profit_dict, damages_firms, damages_dict], json_file)
