#!/usr/bin/python3
""" This module defines the class BaseGeometry """
class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """ This Function raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This Functions validates that value is an integer or <= 0 """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
