#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ If the tuples are smaller than 2, use 0 for the missing values """
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    """ Use only the first 2 integers if the tuples are bigger than 2 """
    a, b = tuple_a[:2]
    c, d = tuple_b[:2]

    """ Add the first and second elements of each tuple """
    result = (a + c, b + d)

    return result

