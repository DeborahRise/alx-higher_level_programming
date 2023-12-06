#!/usr/bin/python3
"""Inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """The function that Inserts text after each line
    with given text
    """
    d_string = ""
    with open(filename) as f:
        for line in f:
            d_string += line
            if search_string in line:
                d_string += new_string
    with open(filename, "w") as f_2:
        f_2.write(d_string)
