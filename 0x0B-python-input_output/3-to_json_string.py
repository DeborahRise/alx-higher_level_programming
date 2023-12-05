#!/usr/bin/python3
"""JSON representation of a string
"""


import json
"""Calling the json module
"""


def to_json_string(my_obj):
    """ serialization
    encoding of a string
    """

    return (json.dumps(my_obj))
