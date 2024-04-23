#!/usr/bin/python3
"""HELLO AGAIJ"""


def minOperations(n):
    """Calculate the minimum number of operations."""
    if n <= 0:
        return 0

    p = 2
    minOp = 0

    while n > 1:
        while n % p == 0:
            minOp += p
            n /= p
        p += 1

    return minOp
