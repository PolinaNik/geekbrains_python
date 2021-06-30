"""Nikitich Polina"""

"""5. Создать (программно) текстовый файл, 
записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить 
её на экран.
"""

from random import randint

# Часть 1 - создаем файл и записываем через пробел рандомные числа
save_to_file = open('text_5.txt', 'w')

list_of_numbers = []
for number in range(100):
    new = str(randint(1, 101))
    list_of_numbers.append(new)

string_of_numbers = ' '.join(list_of_numbers)
save_to_file.write(string_of_numbers)
save_to_file.close()

# Часть 2 - открываем файл подсчитываем сумму чисел

read_file = open('text_5.txt', 'r')
result_string = read_file.readline()
result_list = result_string.split(" ")

result = []
for item in result_list:
    number = int(item)
    result.append(number)

sum_of_numbers = sum(result)
print(f"Сумма чисел - {sum_of_numbers}")

read_file.close()
