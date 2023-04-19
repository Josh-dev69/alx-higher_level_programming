#!/usr/bin/python3

"""
    This module defines a function that writes an object to a text file
"""
import json

def save_to_json_file(my_obj, filename):
    """
        writes object to an text file using the JSON representation
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
