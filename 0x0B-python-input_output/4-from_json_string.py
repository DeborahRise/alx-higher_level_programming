#!/usr/bin/python3
"""JSON deserialization of a string
"""


import json
"""Calling the json module
"""


def from_json_string(my_str):
    """ deserialization
    deencoding of a string
    """

    return (json.load(my_str))
