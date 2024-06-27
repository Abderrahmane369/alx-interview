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

    perim = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:

                if i == 0 or grid[i-1][j] == 0:
                    perim += 1

                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perim += 1

                if j == 0 or grid[i][j - 1] == 0:
                    perim += 1

                if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
                    perim += 1
    return perim
