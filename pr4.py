import numpy as np


# Метод Гаусса с частичным выбором ведущего элемента
def g_ps(a, b):
    matrix = np.c_[a, b]
    tmp = matrix.copy()
    a_rows, a_cols = a.shape

    for index in range(0, a_rows):
        # ищем максимальный элемент по модулю
        index_of_max = np.max(np.argmax([abs(elem) for elem in matrix[index:, index]]))
        # print("column: {} index of max: {} max: {}".format(0, index_of_max, matrix[index_of_max, 0]))

        # если максимальный столбец - не первый, то меняем строки местами
        if index_of_max != 0:
            matrix[index, index:], matrix[index_of_max, index:] = tmp[index_of_max, index:], tmp[index, index:]

        # Все элементы первой строки делят на верхний элемент выбранного столбца.
        matrix[index, index:] = [cx / matrix[index, index] for cx in matrix[index, index:]]

        # Из оставшихся строк вычитают первую строку,
        # умноженную на первый элемент соответствующей строки,
        # с целью получить первым элементом каждой строки (кроме первой) ноль.
        for row in range(index + 1, a_rows):
            matrix[row, index:] = [elem - (first * matrix[row, index]) for elem, first
                                   in zip(matrix[row, index:], matrix[index, index:])]

        # print("row: {} matrix:\n{}".format(index, matrix))
    # Далее проводят такую же процедуру с матрицей, получающейся из исходной матрицы
    # после вычёркивания первой строки и первого столбца.
    # После повторения этой процедуры n-1 раз получают верхнюю треугольную матрицу

    for index in range(a_rows - 1, 0, -1):
        # Вычитаем последнюю строку из остальный строк массива, предаврительно умножив на соотв. коэффициент
        for i in range(0, index):
            matrix[i, :] = [elem - (last * matrix[i, index]) for elem, last in zip(matrix[i, :], matrix[index, :])]
    return matrix
