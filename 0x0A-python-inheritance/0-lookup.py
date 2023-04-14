#!/usr/bin/python3

""" 
    This module defines a function def lookup(obj)
"""
def lookup(obj):
    """ returns a list of available attributes and methods of an object. """
    return dir(obj)
