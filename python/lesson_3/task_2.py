"""Nikitich Polina"""

"""2. Выполнить функцию, которая принимает несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, город 
проживания, email, телефон. Функция должна принимать параметры как 
именованные аргументы. Осуществить вывод данных о пользователе одной 
строкой."""


def get_info(first_name="Polina",
             second_name="Nikitich",
             date_birth="21.07.1995",
             city="Khabarovsk",
             email="polina-nikitich@yandex.ru",
             number=8800):
    return f'User {first_name} {second_name} was born in {date_birth}.\n'f'Now is living in {city}.\nEmail: {email} and mobile number {number}'


print(get_info(first_name="Ivan", second_name="Ivanov",
               date_birth="1.01.1990", city="Moscow",
               email="ivanov@gmail.com", number=5670))

