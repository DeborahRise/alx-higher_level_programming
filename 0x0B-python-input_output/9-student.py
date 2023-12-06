#!/usr/bin/python3
""" a class Student module"""


class Student:
    """for the student."""

    def __init__(self, first_name, last_name, age):
        """Instansiation

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student"""
        return self.__dict__
