#!/usr/bin/python3
"""
get winner of prime number game
"""


def isWinner(x, nums):
    """
    determines winner
    """
    m_wins = 0

    for n in nums:
        p_count = 0
        for i in range(1, n + 1):
            if i > 1:
                prime = True
                for j in range(2, int(i ** 0.5) + 1):
                    if i % j == 0:
                        prime = False
                        break
                p_count += prime
        m_wins += p_count % 2

    b_wins = x - m_wins
    if m_wins > b_wins:
        return "Maria"
    elif b_wins > m_wins:
        return "Ben"
    else:
        return None
