#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for _r in range(len(r) - 1):
            print("{:d}".format(r[_r]), end=' ')
        if len(r) > 0:
            print("{:d}".format(r[-1]))
        else:
            print()
