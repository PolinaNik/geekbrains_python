"""Polina Nikitich"""

##### 1 задание #####

my_list = [1, 'two', 3.0, (4,5,6), [7,8,9], True, {10,11,12}, {13:14, 15:16}]

for i in my_list:
    print(type(i))

##### 2 задание #####

items = input('Напишите через пробел элементы для списка')
my_list = items.split(' ') #строку разбиваем на список
print(my_list)
splitted_list = [my_list[i:i + 2] for i in range(0, len(my_list), 2)] #список разбиваем на пары
new_list = []
#список заполняется новыми значениями, элементы в парах меняются местами
for i in range(len(splitted_list)-1): #берем все пары, кроме последней
    pair = splitted_list[i]
    first = pair[1]
    second = pair[0]
    new_list.append(first)
    new_list.append(second)

#последняя пара проверяется на четность
last_pair = splitted_list[-1]
if len(last_pair) == 2:
    first = last_pair[1]
    second = last_pair[0]
    new_list.append(first)
    new_list.append(second)
else:
    new_list.append(last_pair[0])

print(new_list)

##### 3 задание #####
seasons = {'зима': [12,1,2],
           'весна': [3,4,5],
           'лето': [6,7,8],
           'осень': [9,10,11]}
month = int(input('Введите месяц в виде целого числа от 1 до 12:'))
for key in seasons.keys():
    if month in seasons[key]:
        print(f'Время года - {key}')

##### 4 задание #####
text = input('Напишите несколько слов')
text_list = text.split(' ')
for i in enumerate(text_list, 1):
    if len(i[1]) > 10:
        print(f'{i[0]} {i[1][:10]}')
    else:
        print(f'{i[0]} {i[1]}')

##### 5 задание #####
rating = [7, 5, 3, 3, 2]
print(f'Исходный рейтинг {rating}')
count = 0
while count < 3:
    new_value = int(input('Введите любое натуральное число'))
    rating.append(new_value)
    rating.sort()
    rating.reverse()
    print(f'Новый рейтинг {rating}')
    count += 1

##### 6 задание #####
count = 1
catalog = []
while count < 4:
    user_input = input('Введите через пробел: название товара, цена, количество')
    user_list = user_input.split(' ')
    name = user_list[0]
    price = user_list[1]
    amount = user_list[2]
    info = {"название": name,
            "цена": price,
            "количество": amount,
            "ед": "шт."}
    item = []
    item.append(count)
    item.append(info)
    item = tuple(item)
    catalog.append(item)
    print(f'Сохранено: {item}')
    count += 1

names = []
price = []
amount = []
for i in catalog:
    names.append(i[1]["название"])
    price.append(i[1]["цена"])
    amount.append(i[1]["количество"])

analyse = {"название": names,
           "цена": price,
           "количество": amount}

print(analyse)