#!/usr/bin/python3
"""JSON representation of a string
writes an obj to text file
"""


import json
"""Calling the json module
"""


def save_to_json_file(my_obj, filename):
    """ serialization
    encoding of a string
    """

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
