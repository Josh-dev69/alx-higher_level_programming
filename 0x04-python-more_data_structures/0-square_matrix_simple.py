#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    square_matrix = [[0 for j in range(num_cols)] for i in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            square_matrix[i][j] = matrix[i][j] ** 2

    return square_matrix
