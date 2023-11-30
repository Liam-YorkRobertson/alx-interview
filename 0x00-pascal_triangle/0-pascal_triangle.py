#!/usr/bin/python3
"""
Function to find pascal's triangle integers
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row
    """
    if n <= 0:
        return []

    triangle = []

    for _ in range(n):
        if not triangle:
            row = [1]
        elif len(triangle) == 1:
            row = [1, 1]
        else:
            prev_row = triangle[-1]
            middle_numbers = [prev_row[i - 1] +
                              prev_row[i] for i in range(1, len(prev_row))]
            row = [1] + middle_numbers + [1]
        triangle.append(row)

    return triangle
