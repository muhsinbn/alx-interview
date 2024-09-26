#!/usr/bin/python3
""" Module that rotate a matrix by 90 degrees
"""


def rotate_2d_matrix(matrix):
    """ method to rotate the matrix
    """

    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each row
    for i in range(len(matrix)):
        matrix[i].reverse()
