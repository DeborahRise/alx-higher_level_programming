#!/usr/bin/python3
""" Lets add new attributes
"""


def add_attribute(obj, attribute, value):
    """ The method or function
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
