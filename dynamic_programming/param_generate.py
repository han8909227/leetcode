# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


def generate_parenthesis(n):
    """Take n, output all valid pairs of n param."""
    ans = []

    def backtrack(s='', left=0, right=0):
        """Generate valid pairs using recursive strategy."""
        if len(s) == 2 * n:
            ans.append(s)
            return
        if left < n:  # condition to stop generate left (recursive)
            backtrack(s + '(', left + 1, right)
        if right < left:  # condition to stop generate right (recursive)
            backtrack(s + ')', left, right + 1)

    backtrack()
    return ans
