#!/usr/bin/python3

"""
    This module defines the function def read_file(filename="")
    This function reads the content of its fiule parameter
"""
def read_file(filename=""):
    """ This funtion reads the content of a file """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end='')
