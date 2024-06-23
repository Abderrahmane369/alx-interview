#!/usr/bin/python3
"""OMEGA"""


def rotate_2d_matrix(matrix):
    """generation"""

    for y in range(len(matrix)):
        for x in range(y+1, len(matrix)):
            (matrix[y][x], matrix[x][y]) = (matrix[x][y], matrix[y][x])

    for y in range(len(matrix)):
        matrix[y].reverse()
