# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.


class Node(object):
    """Simple node class."""

    def __init__(self, data):
        """."""
        self.val = data
        self.left = None
        self.right = None


def bst_validator(root):
    """Validate if an input list in a BST."""
    if not root:
        return False

    curr = [root]

    while curr:
        next_level = []
        for node in curr:  # loop through current level
            if node.left:
                if node.val < node.left.val or node.val == node.left.val:  # validate left of curr node
                    return False
                next_level.append(node.left)
            if node.right:
                if node.val > node.right.val or node.val == node.right.val:  # validate right of curr node
                    return False
                next_level.append(node.right)
        curr = next_level  # perculate down level
    return True


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
