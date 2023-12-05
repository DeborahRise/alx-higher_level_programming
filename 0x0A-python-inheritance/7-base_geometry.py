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
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
