#!/usr/bin/python3

"""
    This module defines the function def append_write(filename="", text="")
    This function write to and append string to a file
"""
def append_write(filename="", text=""):
    """ 
        This funtion appends a string at the end of a text file (UTF8) and
        returns the number of characters added:
    """
    with open(filename, "a", encoding="utf-8") as file:
        no_of_char = file.write(text)
    return no_of_char
