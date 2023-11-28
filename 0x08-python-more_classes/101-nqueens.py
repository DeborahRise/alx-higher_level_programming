#!/usr/bin/python3
"""
Solving the Nqueens Puzzle
"""
import sys


def validate():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit():
        N = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N


def safe_space(x, y, array):
    if y in array:
        return (False)
    else:
        return all(abs(array[column] - y) != x - column for column in range(x))


def queen_space(x, column, prev_solver):
    queen_list = []
    for array in prev_solver:
        for y in range(column):
            if safe_space(x, y, array):
                queen_list.append(array + [y])
    return queen_list


def solve(row, column):
    solver = [[]]
    for x in range(row):
        solver = queen_space(x, column, solver)
    return solver


def n_queens():

    N = validate()
    solver = solve(N, N)
    for array in solver:
        d_solution = []
        for x, y in enumerate(array):
            d_solution.append([x, y])
        print(d_solution)


if __name__ == '__main__':
    n_queens()
