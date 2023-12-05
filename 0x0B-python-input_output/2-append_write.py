#!/usr/bin/python3
""" appending a string to a text file
"""


def append_write(filename="", text=""):
    """ Must use with statement
    no file permission
    """

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
