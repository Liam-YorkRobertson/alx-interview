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

    factor_list = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factor_list.append(i)
            n //= i

    if n > 1:
        factor_list.append(n)

    return sum(factor_list)
