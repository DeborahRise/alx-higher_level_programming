#!/usr/bin/python3
"""
 a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
     """ The body of the method """
     if not isinstance(matrix, list):
         raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
     for row in range(len(matrix) - 1):
         if matrix[row] != matrix[row + 1]:
             raise TypeError("Each row of the matrix must have the same size")
     if not isinstance(div, (float, int):
             raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        for r in row:
            round(r/div
