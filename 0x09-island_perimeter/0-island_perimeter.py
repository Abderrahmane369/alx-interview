#!/usr/bin/python3
"""monoga"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    :param grid: List[List[int]] - A rectangular grid where each cell is either 0 (water) or 1 (land).
    :return: int - The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    if len(grid) > 100 or len(grid[0]) > 100:
        raise ValueError("Grid dimensions exceed the maximum allowed size.")

    horiz_perimeter = 0
    vert_perimeter = 0

    for row in grid:
        prev_cell_is_land = False
        for cell in row:
            if cell == 1:
                if not prev_cell_is_land:
                    horiz_perimeter += 1
                prev_cell_is_land = True
            else:
                prev_cell_is_land = False

    for col_index in range(len(grid[0])):
        prev_row_is_land = False
        for row in grid:
            if row[col_index] == 1:
                if not prev_row_is_land:
                    vert_perimeter += 1
                prev_row_is_land = True
            else:
                prev_row_is_land = False

    return 2 * (horiz_perimeter + vert_perimeter)
