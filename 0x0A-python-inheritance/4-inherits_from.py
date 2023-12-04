#!/usr/bin/python3
"""  a function that returns True
if the object is an instance of a class that inherited
(directly or indirectly) from the specified class;
otherwise False
"""


def inherits_from(obj, a_class):
    """ The function
    Args:
    obj: object in question
    a_class: class checked
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
