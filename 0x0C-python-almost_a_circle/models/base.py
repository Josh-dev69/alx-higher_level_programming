#!/usr/bin/python3
""" Defines the class Base """
class Base:
    """ 
        Class Base
        Attribute:
            nb_objects (int):private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialisation of the class Base 
            Args:
                id (int): integer input for id
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
