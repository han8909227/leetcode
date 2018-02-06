# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


def unique_path(m, n):
    """LC62 with dynamic programming."""
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, n):
        for j in range(1, m):
            dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
    return dp[m - 1][n - 1]  # m,n is size index starts at zero


def unique_path_dfs(m, n):
    """LC62 dfs approach."""
    if m < 1 or n < 1:  # stop condition
        return 0
    if m == 1 and n == 1:  # reward condition
        return 1
    return unique_path_dfs(m - 1, n) + unique_path_dfs(m, n - 1)  # to final point must be the total way from top and left combined

