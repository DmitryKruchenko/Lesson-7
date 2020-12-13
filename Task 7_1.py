"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        new_matrix = str()
        if len(self.matrix) == len(other.matrix):
            for line_matrix, line_matrix_other in zip(self.matrix, other.matrix):
                if len(line_matrix) != len(line_matrix_other):
                    return 'Сложение матриц невозможно'

                new_matrix_line = list(map(lambda x, y: x + y, line_matrix, line_matrix_other))
                new_matrix = new_matrix +' '.join([str(elem) for elem in new_matrix_line]) + '\n'
        else:
            return 'Сложение матриц невозможно'
        return new_matrix

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.matrix])


matrix1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix2 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
print(matrix1)
print()
print(matrix2)
print()
print(matrix1 + matrix2)

