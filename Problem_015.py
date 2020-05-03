# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are
# exactly 6 routes to the bottom right corner.
#
# Refer to diagram on https://projecteuler.net/problem=15
#
# How many such routes are there through a 20×20 grid?


def initialise_grid(n):
    grid = [[0]*(n) for i in range(n)]
    return grid


def display_grid(grid):
    for i in grid:
        print(i)


def lattice_paths(n):
    initialGrid = initialise_grid(n)
    row, column = currentPos = startPos = (0, 0)
    endPos = (n, n)

    while currentPos != endPos and column != n:
        row, column = currentPos
        print()

    return

n = 2
print(display_grid(initialise_grid(n+1)))
