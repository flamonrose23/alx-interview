#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    # Transposing elemnts and reversing each row in 1 line
    matrix[:] = [list(row)[::-1] for row in zip(*matrix)]
