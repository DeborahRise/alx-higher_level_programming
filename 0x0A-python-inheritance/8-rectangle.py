#!/usr/bin/python3
""" BaseGeometry module
"""


BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


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

