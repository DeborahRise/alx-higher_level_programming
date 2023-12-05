#!/usr/bin/python3
""" BaseGeometry module
"""


class BaseGeometry:
    """ BaseGeometry class
    """

    def area(self):
        """ A public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Another public instance method
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ The class Rectangle
    """

    def __init__(self, width, height):
        """ Initialization
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
