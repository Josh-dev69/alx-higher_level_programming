#!/usr/bin/python3

""" This module defines the Rectangle class """
class Rectangle:
    """ Representing the class objects """
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
        """ Setter the height of the Rectangle Class """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
