#!/usr/bin/python3
"""This module defines a pascal_triangle(n) function."""

def pascal_triangle(n):
    """ 
        Prints Pascal's Triangle of size n.
        Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    triangles = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangles[i-1][j-1] + triangles[i-1][j])
        row.append(1)
        triangles.append(row)
    return triangles
