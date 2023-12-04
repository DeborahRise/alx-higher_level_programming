#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    checks for instances
    Args:
    obj: the object in question
    a_class: the class to belong
    """

    if type(obj) is a_class:
        return True
    return False
