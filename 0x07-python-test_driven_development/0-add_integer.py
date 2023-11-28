#!/usr/bin/python3
"""
An add_integer module
A function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Adds a and b
    Returns the result
    Raises a TypeError if not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
