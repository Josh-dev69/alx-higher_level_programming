#!/usr/bin/python3

"""
    This module defines the function `say_my_name(first_name, last_name="")`
    this function prints the FullName details(first name and last name.
"""
def say_my_name(first_name, lastname=""):
    """ This function prints My name is <first name> <last name>
    Raises:
        TypeError: first_name must be a string or last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(lastname) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, lastname))
