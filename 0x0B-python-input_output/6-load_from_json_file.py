#!/usr/bin/python3
"""Crates an Object 
from a JSON file
"""


import json
"""Calling the json module
"""


def load_from_json_file(filename):
    """ serialization
    encoding of a string
    """

    with open(filename, "r", encoding='utf-8') as f:
        return (json.load(f))
