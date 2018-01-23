# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


class Node(object):
    """Simple node class."""

    def __init__(self, val):
        """."""
        self.val = val
        self.left = None
        self.right = None


def sum_path(node, target):
    """LC 113."""
    result = []
    curr = []
    _path(node, target, curr, result)
    return result


def _path(node, target, curr, result):
    """Helper."""
    if not node:
        return
    target -= node.val
    if target == 0 and not node.left and not node.right:
        result.append(curr + [node.val])
    if node.left:
        _path(node.left, target, curr + [node.val], result)
    if node.right:
        _path(node.right, target, curr + [node.val], result)


if __name__ == "__main__":
    head = Node(20)
    head.left = Node(10)
    head.left.left = Node(5)
    head.left.right = Node(15)
    head.right = Node(30)
    head.right.left = Node(25)
    head.right.right = Node(35)


