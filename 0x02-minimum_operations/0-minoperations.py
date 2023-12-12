#!/usr/bin/env python3
"""
Function to get the minimum number of operations for the copy and paste task
"""


def minOperations(n):
    """
    Gets the minimum number of operations for the task
    """
    if n < 2:
        return 0

    min_ops = 0
    for i in range(2, n + 1):
        while n % i == 0:
            min_ops += i
            n //= i

    return min_ops
