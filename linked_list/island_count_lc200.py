# Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

# An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).

# Explain and code the most efficient solution possible and analyze its time and space complexities.

# Example:

# input:  binaryMatrix = [ [0,    1,    0,    1,    0],
#                          [0,    0,    1,    1,    1],
#                          [1,    0,    0,    1,    0],
#                          [0,    1,    1,    0,    0],
#                          [1,    0,    1,    0,    1] ]

# output: 6 # since this is the number of islands in binaryMatrix.
#           # See all 6 islands color-coded below.


def count_island(bm):
    """Return number of island(group of 1s) in the matrix."""
    _l = len(bm[0])
    _h = len(bm)
    count = 0

    if not _h:
        return 0

    for r in range(_h):
        for c in range(_l):
            if bm[r][c]:
                count += 1
                dfs(bm, r, c)
    return count


def dfs(bm, r, c):
    """Depth first search on given matrix coordinate."""
    _l = len(bm[0])
    _h = len(bm)

    if r < 0 or c < 0 or r >= _h or c >= _l or bm[r][c] == 0:
        return

    bm[r][c] = 0  # set current to 0 prevent being search again
    dfs(bm, r - 1, c)
    dfs(bm, r + 1, c)
    dfs(bm, r, c - 1)
    dfs(bm, r, c + 1)


if __name__ == '__main__':
    data = [[0, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0]]
