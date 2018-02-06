# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100.


def unique_path_ii(nums):
    """LC63 Dynamic programming."""
    if nums[0][0] == 1:  # cannot start
        return 0
    m = len(nums)
    n = len(nums[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1  # set the start point
    for i in range(1, m):  # change edges since path traversal starts 1,1
        dp[i][0] = dp[i - 1][0] if nums[i][0] == 0 else 0
    for j in range(1, n):  # change edges since path traversal starts 1,1
        dp[0][j] = dp[0][j - 1] if nums[0][j] == 0 else 0

    for i in range(m):  # path traversal
        for j in range(n):
            if nums[i][j] == 1:  # if cannot be passed, erase that possible route
                dp[i][j] = 0
            else:  # if can be passed, accumualte from previous(from top and left)
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]  # the total number of routes


if __name__ == '__main__':
    m = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

