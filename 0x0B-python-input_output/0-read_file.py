#!/usr/bin/python3
""" Reading a text file
"""


def read_file(filename=""):
    """ Must use with statement
    no file permission
    """

    with open(filename, encoding="utf-8") as f:
        dprint = f.read()
        print(dprint, end="")
