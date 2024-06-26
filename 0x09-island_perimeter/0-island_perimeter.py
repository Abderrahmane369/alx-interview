#!/usr/bin/python3
"""monoga"""


def unidimenseV(grid):
    """LOGMON"""
    perlist = []
    a = 0

    for _ in range(len(grid[0])):
        a = 0
        for __ in range(len(grid)):
            if grid[__][_] in {0, 1}:
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
            if grid[_][__] in {0, 1}:
                a |= grid[_][__]
        perlist.append(a)

    return perlist


def island_perimeter(grid):
    """HELLO"""

    if not grid or not grid[0]:
        return 0
    
    # Check if the grid size exceeds the maximum allowed
    if len(grid) > 100 or len(grid[0]) > 100:
        raise ValueError("Grid dimensions exceed the maximum allowed size.")

    return (sum(unidimenseH(grid)) + sum(unidimenseV(grid))) * 2
