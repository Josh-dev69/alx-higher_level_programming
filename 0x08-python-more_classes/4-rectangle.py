#!/usr/bin/python3

""" This module defines the Rectangle class """
class Rectangle:
    """ Representing the class object """
    def __init__(self, width=0, height=0):
        """ Initializing the class """
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

    @height.setter
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
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns a printable string representation of the rectangle """
        rec_str = ""
        if self.__width != 0 and self.__height != 0:
            rec_str += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return rec_str

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
