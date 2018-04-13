"""
Mountain Rainfall
-----------------

Given a list of lists in the form:

[
    [1, 0, 2, 5, 8],
    [2, 3, 4, 7, 9],
]

return a dictionary mapping coordinates to counts of points that flow down
to that point.

For the above example, the only low point is the 0 at (0, 1),
so the result is:

{
    (0, 1): 10,
}
"""

import math


def blank_mat(list_of_lists, value=None):
    return [[
        value for _ in r
    ] for r in list_of_lists]


def safe_get(i, j, landscape, default_value=math.inf):
    # if off the landscape, return inf eg not the lowest
    if (i < 0 or j < 0):
        return default_value
    try:
        return landscape[i][j]
    except IndexError:
        return default_value


def who_is_lowest(i, j, landscape):
    lowest_height = safe_get(i, j, landscape)
    lowest_cell = (i, j)

    for neighbor in [
        ((i - 1), (j - 1)),
        ((i - 1), j),
        ((i - 1), (j + 1)),
        (i, (j - 1)),
        # me
        (i, (j + 1)),
        ((i + 1), (j - 1)),
        ((i + 1), j),
        ((i + 1), (j + 1))
    ]:
        neighbor_height = safe_get(neighbor[0], neighbor[1], landscape)
        if neighbor_height < lowest_height:
            lowest_height = neighbor_height
            lowest_cell = neighbor
    return lowest_cell


def drain(i, j, landscape, accumulation):
    low = who_is_lowest(i, j, landscape)
    if low != (i, j):
        accumulation[low[0]][low[1]] += accumulation[i][j]
        accumulation[i][j] = 0
        drain(low[0], low[1], landscape, accumulation)


def mountain_rainfall(landscape):
    result = {}
    accumulation = blank_mat(landscape, 1)

    for i in range(len(landscape)):
        for j in range(len(landscape[i])):
            drain(i, j, landscape, accumulation)

    for i in range(len(accumulation)):
        for j in range(len(accumulation[i])):
            if accumulation[i][j] != 0:
                result[(i, j)] = accumulation[i][j]

    return result
