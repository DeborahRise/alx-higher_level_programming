#!/usr/bin/python3
"""
A matrix module
All elements of matrix divided by div

"""


def matrix_divided(matrix, div):
    """ The body of the method
        1st: The matrix
        2nd: The div(ider
        Return: new matrix
        Raise: TypeError, ZeroDivisionError
    """

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(element, int) or isinstance(element, float))
                for element in [number for row in matrix for number in row])):

        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in range(len(matrix) - 1):
        if len(matrix[row]) != len(matrix[row + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    main_mat = []

    for row in matrix:
        new_mat = []
        for i in row:
            new_mat.append(round(i / div, 2))
        main_mat.append(new_mat)

    return main_mat
