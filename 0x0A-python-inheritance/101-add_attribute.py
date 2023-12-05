#!/usr/bin/python3
""" Lets add new attributes
"""


def add_attribute(obj, name, value):
    """ The method or function
    adds new attribute to an object
    if possible
    else: raise TypeError
    """

    if "__dict__" not in dir(obj) or "__slots__" in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
