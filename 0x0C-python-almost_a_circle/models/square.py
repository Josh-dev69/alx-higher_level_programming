#!/usr/bin/python3

"""
Module that defines the Square class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """ A square class
    Attributes:
        __size (int): Size of the square
        __x (int): X coordinate of the square
        __y (int): Y coordinate of the square
        id (int): Id of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new Square. """
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """ Size of the square """
        return self.width
    
    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """ Update the Square attributes.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """ Return a dictionary containing the id, size, x, and y
            attributes of the square """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        
    def __str__(self):
        """ Return a string representation of the square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

