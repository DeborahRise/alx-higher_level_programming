#!/usr/bin/python3
""" A MyInt Module
"""


class MyInt(int):
    """ This inherits from
    int super class
    """

    def __eq__(self, other):

        return self.real != other

    def __ne__(self, other):

        return self.real == other
