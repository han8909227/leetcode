
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

# For example,
# Given n = 3, there are a total of 5 unique BST's.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


def unique_bst(n):
    """."""
    dp = [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        s = 0
        for j in range(i):
            s += dp[j] * dp[i - j - 1]
        dp[i] = s
    # import pdb; pdb.set_trace()
    return dp[-1]

