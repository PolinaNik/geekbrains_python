"""Nikitich Polina"""

"""3. Создать текстовый файл (не программно). Построчно записать 
фамилии сотрудников и величину их окладов (не менее 10 строк). 
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести 
фамилии этих сотрудников. Выполнить подсчёт средней величины дохода 
сотрудников."""

read_file = open('text_3.txt', 'r', encoding='utf-8')
file_obj = read_file.readlines()

salary = []

for item in file_obj:
    item_list = item.split(" ")
    salary.append(float(item_list[1]))
    if float(item_list[1]) < 20000:
        print(f"{item_list[0]} имеет оклад менее 20000, сотрудник получает {item_list[1]}")

average_salary = round(sum(salary) / len(salary), 2)
print(f"Средняя зарплата {average_salary}")

read_file.close()
