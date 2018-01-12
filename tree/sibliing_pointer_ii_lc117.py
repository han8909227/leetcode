# Follow up for problem "Populating Next Right Pointers in Each Node".

# What if the given tree could be any binary tree? Would your previous solution still work?

# Note:

# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL


class Node(object):
    """Simple node class."""

    def __init__(self, data):
        """."""
        self.data = data
        self.left = None
        self.right = None


def connect2(node):
    """LC 117."""
    while node:
        curr = node
        while curr:
            if curr.left and curr.right:  # with both children
                curr.left.next = curr.right

            if curr.next:
                if curr.left and not curr.right:  # curr single child left
                    if curr.next.left:  # next single child left
                        curr.left.next = curr.next.left
                    elif curr.next.right:  # next single child right
                        curr.left.next = curr.next.right
                elif curr.right and not curr.left:  # curr single child right
                    if curr.next.left:
                        curr.right.next = curr.next.left
                    elif curr.next.right:
                        curr.right.next = curr.next.right

            curr = curr.next  # loop across
        if node.right and not node.left:  # single child right
            node = node.right
        else:  # single child left or both or none(all fine)
            node = node.left

