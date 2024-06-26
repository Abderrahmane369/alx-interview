#!/usr/bin/python3
"""monoga"""


def unidimenseV(grid):
    """LOGMON"""
    perlist = []
    a = 0

    for _ in range(len(grid[0])):
        a = 0
        for __ in range(len(grid)):
            a |= grid[__][_]
        perlist.append(a)

    return perlist


def unidimenseH(grid):
    """lllll"""
    perlist = []
    a = 0

    for _ in range(len(grid)):
        a = 0
        for __ in range(len(grid[0])):
            a |= grid[_][__]
        perlist.append(a)

    return perlist


def island_perimeter(grid):
    """HELLO"""
    
    if len(grid) > 100 or len(grid[0]) > 100:
        return;

    return (sum(unidimenseH(grid)) + sum(unidimenseV(grid))) * 2
