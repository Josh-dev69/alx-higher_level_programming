#!/usr/bin/python3

""" This module defines a function def lookup(obj)
    def lookup(obj): returns the list of available attributes
    and methods of an object
"""
def lookup(obj):
    """
        This function takes an object as parameter and returns a list of
        its available attributes and methods.
    """
    return dir(obj)
