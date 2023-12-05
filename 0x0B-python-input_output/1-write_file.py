#!/usr/bin/python3
""" writing a string to a text file
"""


def write_file(filename="", text=""):
    """ Must use with statement
    no file permission
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
