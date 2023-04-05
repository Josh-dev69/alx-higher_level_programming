#!/usr/bin/python3

"""
    This module defines the function `text_indentation(text)`.
    This Function prints 2 new lines after  each of these
    characters: ., ? and :
"""

def text_indentation(text):
    """ Prints a text with 2 new lines after each of these
    characters: ., ? and :
    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    sentence = ""
    i = 0
    while i < len(text):
        if text[i] != "." and text[i] != "?" and text[i] != ":":
            sentence = sentence + text[i]
        else:
            sentence += text[i]
            print(sentence)
            print()
            sentence = ""
            while i < (len(text) - 1) and text[i+1] == " ":
                i += 1
        i += 1
    print(sentence, end="")
