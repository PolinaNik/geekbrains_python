"""Nikitich Polina"""

"""5. Программа запрашивает у пользователя строку чисел, разделённых 
пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь 
может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы 
завершается. Если специальный символ введён после нескольких чисел, то 
вначале нужно добавить сумму этих чисел к полученной ранее сумме и после
этого завершить программу.
"""

def calculate_numbers():
    sum_list = 0
    while True:
        user_string = input('Введите числа через пробел')
        if user_string == "q":
            break
        user_list = user_string.split(' ')
        if 'q' in user_list:
            end = user_list.index('q')
            user_list = [int(x) for x in user_list[:end]]
            sum_list0 = sum(user_list)
            sum_list += sum_list0
            print(sum_list)
            break
        else:
            user_list = [int(x) for x in user_list]
            sum_list0 = sum(user_list)
            sum_list += sum_list0
            print(sum_list)

calculate_numbers()

