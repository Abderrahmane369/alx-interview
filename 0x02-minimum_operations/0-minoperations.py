#!/usr/bin/python3
"""HELLO AGAIJ"""


def minOperations(n):
    """Calculate the minimum number of operations."""
    if n <= 1:
        return 0

    operations = 0
    p = 2

    while n > 1:
        while n % p == 0:
            operations += p
            n /= p
        p += 1

    return operations
