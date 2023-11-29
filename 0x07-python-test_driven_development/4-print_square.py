#!/usr/bin/python3
"""
A print square module
using '#'

"""


def print_square(size):
    """
    Body of function
    Args:
    Param1: Type int the size of the square
    Raises: TypeError and ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
