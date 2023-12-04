#!/usr/bin/python3
""" This module prints
in ascending order
"""


class MyList(list):
    """ This class inherits from
            list class """

    def __init__(self):
        """ Initializes the object
        """
        super().__init__()

    def print_sorted(self):
        """ sort the list in ascending order
        """
        print(sorted(self))
