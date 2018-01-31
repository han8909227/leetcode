# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


class Node(object):
    """Simple node class."""

    def __init__(self, val):
        """."""
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        """."""
        return str(self.val)


def path_sum(head, s):
    """."""
    count = 0
    _helper(head, s, count)
    return count


def _helper(node, s, count):
    """."""
    if s == 0:
        count += 1
        return
    if node.left:
        _helper(node.left, s - node.left.val, count)
    if node.right:
        _helper(node.right, s - node.right.val, count)


if __name__ == "__main__":
    head = Node(20)
    head.left = Node(10)
    head.left.left = Node(5)
    head.left.right = Node(15)
    head.right = Node(30)
    head.right.left = Node(25)
    head.right.right = Node(35)
