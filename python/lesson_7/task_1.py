"""Nikitich Polina"""

"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса 
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной
 схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица. 
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой 
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

input_data_1 = [[7, 2, 4], [5, 4, 10], [3, 8, 15]]  # входные данные для первой матрицы
input_data_2 = [[20, 1, 78], [10, 5, 22], [7, 8, 15]]  # входные данные для второй матрицы


class Matrix:
    """Класс, формирующий матрицу"""

    def __init__(self, matrix):
        self.matrix = matrix

    def numbers_to_string(self, matrix):
        """Функция, преобразующая цифры списка в строки.
        Например:
        [[1, 2], [3, 4]] -> [['1', '2'], ['3', '4']]"""

        self.result = []
        for row in matrix:
            lst = []
            for item in row:
                lst.append(str(item))
            self.result.append(lst)
        return self.result

    def __add__(self, other):
        """Сложение двух матриц"""

        sum_matrix = []
        for number_row, row in enumerate(self.matrix):
            sum_item = []
            for number_item, item in enumerate(row):
                new = item + other.matrix[number_row][number_item]
                sum_item.append(new)
            sum_matrix.append(sum_item)
        formated_matrix = self.numbers_to_string(sum_matrix)
        formated_list = [' '.join(item) for item in formated_matrix]
        indent_list = '\n'.join(formated_list)
        return indent_list

    def __str__(self):
        """Вывод матрицы в читаемом виде"""

        input_list = self.numbers_to_string(self.matrix)
        formated_list = [' '.join(item) for item in input_list]
        indent_list = '\n'.join(formated_list)
        return indent_list


matrix_1= Matrix(input_data_1)
print(f"Матрица первая:\n{matrix_1}")
matrix_2 = Matrix(input_data_2)
print(f"Матрица вторая:\n{matrix_2}")

print(f"Сумма матриц:\n{matrix_1 + matrix_2}")
