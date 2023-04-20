#!/usr/bin/python3
"""Defines unittests for Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class."""

    def test_valid_init(self):
        """Test for valid 'Rectangle.__init__()' initialization."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

    def test_invalid_init(self):
        """ Test for invalid 'Rectangle.__init__()' initialization """
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, "5")

    def test_area(self):
        """Test Rectangle.area()."""
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.area(), 15)

    def test_display(self):
        """Test Rectangle.display()."""
        r1 = Rectangle(2, 3)
        r1.display()
        self.assertEqual(r1.display(), None)

    def test_update_args(self):
        """Test for *args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_update_kwargs(self):
        """ Test for **kwargs """
        r1.update(id=89)
        self.assertEqual(r1.id, 89)
        r1.update(width=2)
        self.assertEqual(r1.width, 2)
        r1.update(height=3)
        self.assertEqual(r1.height, 3)
        r1.update(x=4)
        self.assertEqual(r1.x, 4)
        r1.update(y=5)
        self.assertEqual(r1.y, 5)
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

    def test_to_dictionary(self):
        """Test Rectangle.to_dictionary()."""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': r1.id, 'height': 2, 'width': 10}
        self.assertEqual(r1_dict, expected)

    def test_str(self):
        """Test Rectangle.__str__()."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6)")

if __name__ == '__main__':
    unittest.main()

