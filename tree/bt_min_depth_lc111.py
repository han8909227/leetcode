# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


class Node(object):
    """Simple node class."""

    def __init__(self, data):
        """."""
        self.data = data
        self.left = None
        self.right = None


def min_depth(head):
    """Find min depth of a binary tree."""
    if head is None:
        return 0
    if head.left is None and head.right is None:
        return 1  # single level
    else:
        return min(min_depth(head.left), min_depth(head.right)) + 1


if __name__ == "__main__":
    head = Node(20)
    head.left = Node(10)
    head.left.left = Node(5)
    head.left.right = Node(15)
    head.right = Node(30)
    head.right.left = Node(25)
    head.right.right = Node(35)
    head.right.left.left = Node(22)
    head.right.left.right = Node(28)
    head.right.right.left = Node(32)
    head.right.right.right = Node(38)
    head.left.left.left = Node(2)
    head.left.left.right = Node(8)
    head.left.right.left = Node(12)
    head.left.right.right = Node(18)
