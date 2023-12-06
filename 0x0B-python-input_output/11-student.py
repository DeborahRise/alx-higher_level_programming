#!/usr/bin/python3
"""A class Student"""


class Student:
    """a student in i give ."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)
