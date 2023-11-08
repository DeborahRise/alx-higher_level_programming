#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for r in matrix:
        matrix2.append([x ** 2 for x in r])
    return matrix2
