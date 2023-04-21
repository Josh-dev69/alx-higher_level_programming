#!/usr/bin/python3
"""
Module that defines the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    A rectangle class

    Args:
        Base (class): Base class

    Attributes:
        __width (int): Width of the rectangle
        __height (int): Height of the rectangle
        __x (int): X coordinate of the rectangle
        __y (int): Y coordinate of the rectangle
        id (int): Id of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """X coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle with '#' characters"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the rectangle's attributes"""
        if args and len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i >= len(attrs):
                    break
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
