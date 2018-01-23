
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


class Node(object):
    """Simple node class."""

    def __init__(self, val):
        """."""
        self.val = val
        self.left = None
        self.right = None


def path_sum(node, target):
    """LC 112."""
    if not node:
        return False

    if not node.left and not node.right:
        return node.val == target

    return path_sum(node.left, target - node.val) or path_sum(node.right, target - node.val)


if __name__ == "__main__":
    head = Node(20)
    head.left = Node(10)
    head.left.left = Node(5)
    head.left.right = Node(15)
    head.right = Node(30)
    head.right.left = Node(25)
    head.right.right = Node(35)

