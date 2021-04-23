"""Nikitich Polina"""

"""7. Продолжить работу над заданием. В программу должна попадать строка 
из слов, разделённых пробелом. Каждое слово состоит из латинских букв в 
нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово 
должно начинаться с заглавной буквы. Используйте написанную ранее функцию
int_func().
"""

def int_func(*args):
    capitalize_list = []
    for i in args:
        splitted_item = i.split(' ')
        for item in splitted_item:
            new = item.capitalize()
            capitalize_list.append(new)
    return ' '.join(capitalize_list)

print(int_func('test', 'one more test'))