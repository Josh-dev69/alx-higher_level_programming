#!/usr/bin/python3

""" This module defines a class MyList. """
class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
        This method prints the list sorted in ascending order.
        """
        print(sorted(self))
