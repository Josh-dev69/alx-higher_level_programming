#!/usr/bin/python3

"""
    This module defines the function print_square(size)
    This function prints a square with the character '#'
    You are not allowed to import any module
"""

def print_square(size):
    """ Returns a square of '#' character(s)
    where size is the number of the '#' characters
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integer
    """
    if not(isinstance(size, int) or isinstance(size, float)
            and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#",end="")
        else:
            print("")
