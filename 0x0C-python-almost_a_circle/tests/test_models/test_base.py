#!/usr/bin/python3
""" My Test Module for the
Base Class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import inspect


class TestBase(unittest.TestCase):
    """ Introducing the unittest Test case """

    def test_id(self):
        """ First tests on id argument"""

        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        base3 = Base(12)
        self.assertEqual(base3.id, 12),

        base4 = Base()
        self.assertEqual(base4.id, 3)

    def test_single_id(self):
        self.assertEqual(Base(7).id, 7)

    if __name__ == "__main__":
        unittest.main()
