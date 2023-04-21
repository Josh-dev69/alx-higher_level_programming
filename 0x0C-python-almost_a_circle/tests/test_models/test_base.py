#!/usr/bin/python3

""" Defines unittests for base.py. """

import unittest
import os
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the number of objects before each test."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test that the id attribute is set correctly."""
        r1 = Rectangle(10, 10)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 10)
        self.assertEqual(r2.id, 2)
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        s2 = Square(10)
        self.assertEqual(s2.id, 2)

    def test_json_string(self):
        """Test that to_json_string produces the correct output."""
        r1 = Rectangle(10, 10, 10, 10)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"x": 10, "width": 10, "id": 1, "height": 10, "y": 10}]')

    def test_save_to_file(self):
        """Test that save_to_file writes the correct output to a file."""
        r1 = Rectangle(10, 10, 10, 10)
        r2 = Rectangle(20, 20, 20, 20)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            contents = file.read()
        expected_output = '[{"x": 10, "width": 10, "id": 1, "height": 10, "y": 10}, {"x": 20, "width": 20, "id": 2, "height": 20, "y": 20}]'
        self.assertEqual(contents, expected_output)

    def test_from_json_string(self):
        """Test that from_json_string produces the correct output."""
        json_string = '[{"x": 10, "width": 10, "id": 1, "height": 10, "y": 10}, {"x": 20, "width": 20, "id": 2, "height": 20, "y": 20}]'
        output = Base.from_json_string(json_string)
        expected_output = [{"x": 10, "width": 10, "id": 1, "height": 10, "y": 10}, {"x": 20, "width": 20, "id": 2, "height": 20, "y": 20}]
        self.assertEqual(output, expected_output)

    def test_create(self):
        """Test that create produces the correct output."""
        dictionary = {"x": 10, "y": 20, "id": 1, "width": 30, "height": 40}
        r1 = Rectangle.create(**dictionary)
        expected_output = "[Rectangle] (1) 10/20 - 30/40"
        self.assertEqual(str(r1), expected_output)

    def test_load_from_file(self):
        """Test that load_from_file produces the correct output."""
        r1 = Rectangle(10, 10, 10, 10)
        r2 = Rectangle(20, 20, 20, 20)
        Rectangle.save_to_file([r1, r2])

