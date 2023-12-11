#!/usr/bin/python3
""" a new test file
"""


import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """ all different testcase for the Square class"""

    def test_size(self):
        sqr = Square(7, 7, 3, 2)
        self.assertEqual(sqr.width, 7)
        self.assertEqual(sqr.height, 7)
        self.assertEqual(sqr.x, 7)
        self.assertEqual(sqr.y, 3)

    def test_ifsqr(self):
        self.assertIsInstance(Square(10, 7), Base)

    def test_setter(self):
        sqr = Square(7, 3, 2)
        with self.assertRaises(TypeError):
            sqr.width = "7"
        with self.assertRaises(TypeError):
            sqr.height = "7"
        with self.assertRaises(ValueError):
            sqr.width = 0
        with self.assertRaises(ValueError):
            sqr.height = -1

    def test_instantiation(self):
        sqr = Square(7, 1, 2)
        with self.assertRaises(ValueError):
            Square(-7, -1, -2)

    def test_update(self):
        sqr = Square(7, 10, 1, 2)
        sqr.update(7, 10, 1, 2)
        self.assertEqual(sqr.id, 7)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 1)
        self.assertEqual(sqr.y, 2)

    def setUp(self):
        self.square = Square(10, 2, 1)

    def test_to_dictionary(self):
        square_dict = self.square.to_dictionary()
        self.assertEqual(square_dict, {'id': 8, 'size': 10, 'x': 2, 'y': 1})

    def test_update_from_dictionary(self):
        new_square = Square(1, 1)
        new_square.update(**self.square.to_dictionary())
        self.assertEqual(new_square.id, self.square.id)
        self.assertEqual(new_square.size, self.square.size)
        self.assertEqual(new_square.x, self.square.x)
        self.assertEqual(new_square.y, self.square.y)
