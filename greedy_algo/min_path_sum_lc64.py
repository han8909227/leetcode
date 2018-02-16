
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.


def min_path_sum(nums):
    """LC64."""
    m = len(nums)
    n = len(nums[0])

    dp = [0 for __ in range(n)]
    dp[0] = nums[0][0]  # start point 1st val
    for j in range(1, n):  # start at pos 1, 0 as start point
        dp[j] = dp[j - 1] + nums[0][j]  # steps for going across
    for i in range(1, m):
        dp[0] += nums[i][0]  # start point going 1 step down
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j - 1]) + nums[i][j]  # cost between going straigh down from above or from left
    return dp[-1]  # cost to reach nums[-1][-1]

