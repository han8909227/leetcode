# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]


class Node(object):
    """Simple node class."""

    def __init__(self, val):
        """."""
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def path(head):
    """LC 257."""
    result = []
    _path(head, result)
    return result


def _path(node, result, temp=None):
    """."""
    if not temp:
        temp = []

    if not node.left and not node.right:
        result.append(temp + [node])
        return
    if node.left:
        _path(node.left, result, temp + [node])
    if node.right:
        _path(node.right, result, temp + [node])


if __name__ == "__main__":
    head = Node(20)
    head.left = Node(10)
    head.left.left = Node(5)
    head.left.right = Node(15)
    head.right = Node(30)
    head.right.left = Node(25)
    head.right.right = Node(35)
