"""Nikitich Polina"""

##### Задание 1 #####

number = 5
str_value = 'Это строка'
float_value = 5.7889
bool_value = True

print(f'Это число: {number}')
print('x'*15)
print(str_value)
print('x'*15)
print(f'А это число с плавающей точкой: {str(float_value)}')
print('x'*15)
print(f'А это булевое значение: {bool_value}')
print('x'*15)

my_input = input('Напишите что-нибудь:')
print(f"Вы только что написали вот это: {my_input}")
my_input = input('Теперь пожалуйста напишите число:')

try:
    number = int(my_input)
    print(f"Ваше число: {number}")
except ValueError:
    print("Извините, но вы написали не число, а что-то другое...")

input_time = input('Напишите значение времени в секундах:')

##### 2 #####

try:
    seconds = int(input_time)
    if seconds <= 86400:
        hour = int(seconds // 3600)
        remainder = seconds % 3600
        minute = int(remainder // 60)
        second = int(minute % 60)
        full_time = str(hour)+':'+str(minute)+':'+str(second)
        time_list = full_time.split(':')
        time_list = [x if len(x)==2 else '0'+x for x in time_list]
        full_time = ':'.join(time_list)
        print(f'Время {full_time}')
    if seconds > 86400:
        day = int(seconds // 86400)
        remainder = seconds % 86400
        hour = int(remainder // 3600)
        remainder2 = remainder % 3600
        minute = int(remainder2 // 60)
        second = int(remainder2 % 60)
        full_time = str(hour)+':'+str(minute)+':'+str(second)
        time_list = full_time.split(':')
        time_list = [x if len(x)==2 else '0'+x for x in time_list]
        full_time = ':'.join(time_list)
        print(f'{day} дней и время {full_time}')
except ValueError:
    print("Извините, но вы написали не число, а что-то другое...")

##### 3 #####

number = input('Пожалуйста введите значение n:')
try:
    n = int(number)
    nn = int(number+number)
    nnn = int(number+number+number)
    calculated = n + nn + nnn
    print(f'Результат {calculated}')
except ValueError:
    print("Извините, но вы написали не число, а что-то другое...")

##### 4 #####

number = input('Узнаем максимальную цифру в вашем числе, введите число:')
try:
    n = int(number)
    big = 0
    len_number = len(number)
    i = 0
    while i < len_number:
        int_number = int(number[i])
        if int_number > big:
            big = int_number
            i+=1
        else:
            i+=1
    print(f'Наибольшая цифра {big}')
except ValueError:
    print("Извините, но вы написали не число, а что-то другое...")

##### 5 #####

earnings = input('Напишите значение выручки фирмы:')
costs = input('Напишите значение издержек у фирмы:')

try:
    earnings = int(earnings)
    costs = int(costs)
    if earnings > costs:
        print('Здороро! Выручка больше издержек')
        profit = earnings - costs
        print(f'Ваша прибыль {profit}')
        workers = input('Сколько сотрудников работает в компании?')
        try:
            workers = int(workers)
            profit_per_worker = profit / workers
            print(f'Доход на каждого сотрудника составил {str(profit_per_worker)}')
        except:
            print("Извините, но вы написали не число, а что-то другое...")
    else:
        print('К сожалению издержки больше чем выручка :(')
except ValueError:
    print("Извините, но вы написали не число, а что-то другое...")

##### 6 #####

a = int(input('Пожалуйста введите число a:'))
b = int(input('Пожалуйста введите число b (число b должно быть больше a):'))

count = 1
while a < b:
    a += 0.1 * a
    count += 1

print(f'Спортсмен достигнет своего результата на {count} день')