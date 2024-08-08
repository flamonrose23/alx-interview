#!/usr/bin/python3

"""
Writing method calculating by using minimum of operations
"""


def minOperations(n):
    """
    This function will calculate fewest number of operations needed to result
    in exactly n H characters in the file.
    """

    second = 1
    first = 0
    number = 0
    while second < n:
        remainder = n - second
        if (remainder % second == 0):
            first = second
            second += first
            number += 2
        else:
            second += first
            number += 1
    return number
