#!/usr/bin/python3
""" A test suite for Rectangle
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Instsnces to check Rectangle
    """

    def test_instantiation(self):
        rec = Rectangle(7, 3)
        self.assertEqual(rec.width, 7)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)

    def test_setters(self):
        with self.assertRaises(TypeError):
            Rectangle("7", 3)
        with self.assertRaises(TypeError):
            Rectangle(7, "3")
        with self.assertRaises(TypeError):
            rec = Rectangle(7, 3)
            rec.x = "value"
        with self.assertRaises(TypeError):
            rec = Rectangle(7, 5)
            rec.y = "value"
        with self.assertRaises(TypeError):
            Rectangle(7.7, 3.3)

    def test_setter(self):
        rec = Rectangle(7, 3)
        rec.width = 9
        rec.height = 5
        rec.x = 3
        rec.y = 1
        self.assertEqual(rec.width, 9)
        self.assertEqual(rec.height, 5)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 1)

    def test_wrongtype(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(7, 5)
            rec.width = "value"
        with self.assertRaises(TypeError):
            rec = Rectangle(7, 5)
            rec.height = "value"

    def test_wrongvalue(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(7, 5)
            rec.width = 0
        with self.assertRaises(ValueError):
            rec.height = 0
        with self.assertRaises(ValueError):
            rec.x = -3
        with self.assertRaises(ValueError):
            rec.y = -6
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            rec = Rectangle(-4, -3, -7, -4)

    def test_area(self):
        rec = Rectangle(5, 10)
        self.assertEqual(rec.area(), 50)

    def test_str(self):
        rec = Rectangle(5, 10, 2, 1, 12)
        self.assertEqual(str(rec), "[Rectangle] (12) 2/1 - 5/10")

    def test_strValueError(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 10, 2, 1, 12)

    def test_update(self):
        rec = Rectangle(90, 10, 5, 2, 1)
        rec.update(91, 11, 6, 3, 2)
        self.assertEqual(rec.id, 91)
        self.assertEqual(rec.width, 11)
        self.assertEqual(rec.height, 6)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 2)

        rec.update(92, 12)
        self.assertEqual(rec.id, 92)
        self.assertEqual(rec.width, 12)
        self.assertEqual(rec.height, 6)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 2)

        rec.update(91, 11, 9, 5, 2)
        self.assertEqual(rec.id, 91)
        self.assertEqual(rec.width, 11)
        self.assertEqual(rec.height, 9)
        self.assertEqual(rec.x, 5)
        self.assertEqual(rec.y, 2)

    def test_update2(self):
        rec = Rectangle(90, 10, 5, 2, 1)
        rec.update(height=10)
        self.assertEqual(rec.height, 10)

        rec.update(width=5, x=4)
        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.x, 4)

        rec.update(y=1, x=2, height=3, width=4, id=5)
        self.assertEqual(rec.y, 1)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.width, 4)
        self.assertEqual(rec.id, 5)

        def setUp(self):
            self.rectangle = Rectangle(10, 2, 1, 9)

        def test_to_dictionary(self):
            rectangle_dict = self.rectangle.to_dictionary()
            self.assertEqual(rectangle_dict, {
                'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9
                })

        def test_update_from_dictionary(self):
            new_rectangle = Rectangle(1, 1)
            new_rectangle.update(**self.rectangle.to_dictionary())
            self.assertEqual(new_rectangle.id, self.rectangle.id)
            self.assertEqual(new_rectangle.width, self.rectangle.width)
            self.assertEqual(new_rectangle.height, self.rectangle.height)
            self.assertEqual(new_rectangle.x, self.rectangle.x)
            self.assertEqual(new_rectangle.y, self.rectangle.y)


if __name__ == "__main__":
    unittest.main()
