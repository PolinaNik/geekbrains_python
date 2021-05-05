"""Nikitich Polina"""

"""Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую 
построчно данные. При этом английские числительные должны 
заменяться на русские. Новый блок строк должен записываться в новый
 текстовый файл.
"""

russian_numerals = ['один', 'два', 'три', 'четыре']

write_file = open('text_4_rus.txt', 'w', encoding='utf-8')

with open('text_4.txt', 'r') as read_file:
    read_lines = read_file.readlines()
    for number, item in enumerate(read_lines):
        item_list = item.split(" ")
        if len(item_list) == 3:
            rus_name = russian_numerals[number]
            rus_list = [rus_name] + [item_list[2]]
            rus_item = " — ".join(rus_list)
            print(rus_item)
            write_file.write(rus_item)

write_file.close()
