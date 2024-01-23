#!/usr/bin/python3
"""
rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotates matrix 90 degrees
    """
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated_matrix[i][j]
