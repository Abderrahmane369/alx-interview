#!/usr/bin/python3
"""AAAA"""
import math

def _factorial(n):
    """AAAA"""
    r = 1

    for _ in range(1, n + 1):
        r *= _

    return r


def pascal_triangle(n):
    """AAAAAA"""
    if n <= 0:
        return []

    arr = []

    for i in range(n):
        _r = []
        for j in range(n):
            _r.append(math.floor(_factorial(i) / (_factorial(j) * _factorial(i - j))))
        
        for _ in range(n):
            if 0 in _r:
                _r.remove(0)
        
    
        arr.append(_r)
    
    if n > 1:
        arr[0].pop()
        
    return arr
