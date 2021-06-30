"""Nikitich Polina"""

"""1. Создать программный файл в текстовом формате, записать в него 
построчно данные, вводимые пользователем. Об окончании ввода данных будет
 свидетельствовать пустая строка.
"""

with open('text_1.txt', 'w') as file_text:
    while True:
        user_input = input('Напишите что-нибудь')
        file_text.write(user_input+'\n')
        """скрипт ввода завершается при появле"""
        if user_input == "" or user_input == "q":
            break

with open('text_1.txt', 'r') as file_text:
    print('Ваш текст, который вы ввели выше:')
    print(file_text.read())
