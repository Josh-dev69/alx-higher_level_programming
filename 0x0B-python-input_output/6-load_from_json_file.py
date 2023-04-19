#!/usr/bin/python3

"""
    This module defines a function that creates an Object from a “JSON file”
"""
import json

def load_from_json_file(my_obj, filename):
    """
        creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        return json.load(my_file)
~                                          
