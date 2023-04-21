#!/usr/bin/python3

""" define the unittest for square.py """

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        """ initializes three instances of the Square class """
        self.s1 = Square(5)
        self.s2 = Square(7, 1, 2, 3)
        self.s3 = Square(10, 2, 3, 4)

    def test_init(self):
        """ tests if the instances are initialized correctly """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s2.size, 7)
        self.assertEqual(self.s2.x, 1)
        self.assertEqual(self.s2.y, 2)
        self.assertEqual(self.s3.id, 4)
        self.assertEqual(self.s3.size, 10)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s3.y, 3)

    def test_str(self):
        """ tests if the string representation of the instances is correct """
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(self.s2), "[Square] (2) 1/2 - 7")
        self.assertEqual(str(self.s3), "[Square] (4) 2/3 - 10")

    def test_update(self):
        """ tests if the instances can be updated correctly """
        self.s1.update(2)
        self.assertEqual(self.s1.id, 2)
        self.s2.update(3, 6, 2, 4)
        self.assertEqual(self.s2.id, 3)
        self.assertEqual(self.s2.size, 6)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 4)
        self.s3.update(size=15, y=6)
        self.assertEqual(self.s3.size, 15)
        self.assertEqual(self.s3.y, 6)

    def test_to_dictionary(self):
        """ tests if the dictionary representation of the instances is correct """
        d1 = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        d2 = {'id': 2, 'size': 7, 'x': 1, 'y': 2}
        d3 = {'id': 4, 'size': 10, 'x': 2, 'y': 3}
        self.assertEqual(self.s1.to_dictionary(), d1)
        self.assertEqual(self.s2.to_dictionary(), d2)
        self.assertEqual(self.s3.to_dictionary(), d3)

    def test_size_getter_setter(self):
        """ tests if the size attribute of the instances can be accessed and
        modified correctly """
        self.assertEqual(self.s1.size, 5)
        self.s1.size = 10
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s1.width, 10)
        self.assertEqual(self.s1.height, 10)
        with self.assertRaises(ValueError):
            self.s1.size = -5

    def test_update_kwargs_with_args(self):
        """ tests if an error is raised when trying to update the instance with both
        args and kwargs """
        with self.assertRaises(TypeError):
            self.s1.update(1, 5, 0, 0, size=10, x=2)


if __name__ == "__main__":
    unittest.main()

