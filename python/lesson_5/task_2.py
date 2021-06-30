"""Nikitich Polina"""

"""2. Создать текстовый файл (не программно), сохранить в нём 
несколько строк, выполнить подсчёт строк и слов в каждой строке."""

with open('text_2.txt', 'r', encoding='utf-8') as read_file:
    opened_file = read_file.readlines()
    len_lines = len(opened_file)
    for i, element in enumerate(opened_file):
        element_list = element.split(" ")
        len_row = len(element_list)
        print(f"В строке {i + 1} - {len_row} слов")
    print(f"Всего {len_lines} строк в файле")
