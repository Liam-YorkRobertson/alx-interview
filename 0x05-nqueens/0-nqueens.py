#!/usr/bin/python3
"""
solves nqueens problem
"""
import sys


def nqueens(board, row, n):
    """
    checks if queen can be placed in the position
    """
    if row == n:
        print([list(pair) for pair in enumerate(board)])
    else:
        for col in range(n):
            if all(board[i] != col and
                   board[i] - i != col - row and
                   board[i] + i != col + row
                   for i in range(row)):
                nqueens(board + [col], row + 1, n)


def main():
    """
    main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens([], 0, n)


if __name__ == "__main__":
    main()
