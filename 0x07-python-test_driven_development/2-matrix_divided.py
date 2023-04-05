#!/usr/bin/python3

""" This module defines a function ``matrix_divided(matrix, div)``
    that performs scalar division of matrix.
    You are not allowed to import any module
"""
def matrix_divided(matrix, div):
    """ Return float numbers for the scalar(integer) division of the
    Matrix.
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix or
            not all(isinstance(elem, int) or isinstance(elem, float))
                for elem in [num for row in matrix for num in row])):
                raise TypeError("Matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
