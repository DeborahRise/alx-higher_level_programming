#!/usr/bin/python3
""" My first clase
Base
"""

import json


class Base:
    """ instantiation of the Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ The base class constructor
        method
        """
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the json rep of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string rep to file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dictionaries))
