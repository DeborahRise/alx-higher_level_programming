#!/usr/bin/python3

def lookup(obj):
    """
    a function that returns the list of available
    attributes and methods of an object:
    """

    return [getattr(obj, name) for name in dir(obj)]
