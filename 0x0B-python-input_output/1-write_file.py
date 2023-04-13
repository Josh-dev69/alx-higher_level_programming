#!/usr/bin/python3

"""
    This module defines the function def write_file(filename="", text=""):
    This function write to and reads the content of its file parameter
"""
def write_file(filename="", text=""):
    """ 
        This funtion writes a string to a text file (UTF8) and returns
        the number of characters written 
    """
    with open(filename, "w", encoding="utf-8") as file:
        no_of_char = file.write(text)
    return no_of_char
