#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for _r in range(len(r) - 1):
            print("{}".format(r[_r]), end=' ')
        if len(r) > 0:
            print("{}".format(r[-1]))
        else:
            print()
