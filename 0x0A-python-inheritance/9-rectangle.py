#!/usr/bin/python3
""" BaseGeometry module
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ The class Rectangle
    """
    def __init__(self, width, height):
        """ Initialization
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        return self.__width * self.__height

    def __str__(self):

        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string
