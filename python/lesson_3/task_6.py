"""Nikitich Polina"""

"""6. Реализовать функцию int_func(), принимающую слова из маленьких 
латинских букв и возвращающую их же, но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text."""

def int_func(*args):
    capitalize_list = []
    for i in args:
        new = i.capitalize()
        capitalize_list.append(new)
    return ' '.join(capitalize_list)

print(int_func('test', 'one more test'))

