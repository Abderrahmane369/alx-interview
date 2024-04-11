#!/usr/bin/python3
"""AAAA"""


def line(n):
    """AAAA"""
    l = [1]

    for _ in range(n):
        l.append((l[_] * (n - _) // (_ + 1)))

    return l


def pascal_triangle(n):
    """AAAAAA"""
    if n <= 0:
        return []

    arr = []

    for i in range(n):
        arr.append(line(i))

    return arr
