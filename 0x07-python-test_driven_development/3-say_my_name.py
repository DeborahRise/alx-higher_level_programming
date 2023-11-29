#!/usr/bin/python3
"""
A module that prints full names

"""


def say_my_name(first_name, last_name=""):
    """
    The function body
    Args:
    Arg1: type str first name
    Arg2: type str last name
    Raise: TypeError

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
