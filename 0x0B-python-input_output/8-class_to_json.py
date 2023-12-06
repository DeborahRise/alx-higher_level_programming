#!/usr/bin/python3
"""This module defines a function that returns
the dictionary description with simple
data structure (list, dictionary,
"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__
