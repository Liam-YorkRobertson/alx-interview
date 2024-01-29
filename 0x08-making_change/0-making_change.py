#!/usr/bin/python3
"""
module to solve the change problem
"""


def makeChange(coins, total):
    """
    fewest number of coins needed to meet a total
    """
    if total <= 0:
        return 0
    min_coins = {0: 0}
    for amount in range(1, total + 1):
        min_coins[amount] = float('inf')
        for coin in coins:
            if amount >= coin:
                min_coins[amount] = min(min_coins[amount],
                                        min_coins[amount - coin] + 1)
    if min_coins[total] != float('inf'):
        return min_coins[total]
    else:
        return -1
