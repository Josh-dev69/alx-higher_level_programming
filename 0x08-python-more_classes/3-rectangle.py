#!/usr/bin/python3

""" This module defines the Rectangle class """
class Rectangle:
    """ Definining and initializing the class objects """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Function to retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting the width of the Rectangle Class """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Function to retrieve the height """
        return self.__height

    @width.setter
    def height(self, value):
        """ Setting the height of the Rectangle Class """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """ Returns a string representation of the rectangle """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rect_str = ""
            for i in range(self.height):
                rect_str += "#" * self.width
                if i != self.height - 1:
                    rect_str += "\n"
            return rect_str
