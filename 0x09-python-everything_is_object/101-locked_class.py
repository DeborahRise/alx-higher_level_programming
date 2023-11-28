#!/usr/bin/python3
"""A module for a locked class"""


class LockedClass:
    """
    Will only allow the instation of an attribute
    called: first_name
    """

    __slots__ = ["first_name"]
