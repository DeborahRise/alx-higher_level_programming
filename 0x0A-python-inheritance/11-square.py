#!/usr/bin/python3
""" Square module
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ The class Square
    """

    def __init__(self, size):
        """ Initialization
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area method implemented
        """
        return self.__size * self.__size

    def __str__(self):

        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string
