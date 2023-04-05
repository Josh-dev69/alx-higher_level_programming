#!/usr/bin/python3

"""
    This file (0-add_integer.py) is an integer addition module
    It supplies the function prototype def add_integer(a, b=98)
    This Function prototype adds two(2) integers
    You are not allowed to import any module
"""

def add_integer(a, b=98):
    """ Return only the integer addition of a and b
    Typecast Float argument(s) to integer(int) before adding
    Raise TypeError:
        if either of a or b is non-integer or non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    """ Typecasting values of a and b to integer(int) """
    a = int(a)
    b = int(b)

    return a + b
