# Print all edge nodes of a complete binary tree anti-clockwise.
# That is all the left most nodes starting at root, then the leaves left to right and finally all the rightmost nodes.
# In other words, print the boundary of the tree.

# Variant: Print the same for a tree that is not complete.


# Assume we have a binary tree below:

#     _30_
#    /    \
#   10    20
#  /     /  \
# 50    45  35
# The correct solution should print 30, 10, 50, 45, 35, 20.


class Node(object):
    """Simple node class."""

    def __init__(self, data):
        """."""
        self.data = data
        self.left = None
        self.right = None


def boundry_traversal(head):
    """Return boundry traversal of a bt."""
    left = dfs_left_nodes(head)[:-1]  # don't want tail, will traversed in bottom
    bottom = dfs_children_only(head)
    right = dfs_right_nodes(head)[::-1]  # reverse to match counter clock pattern
    right = right[:-1]  # don't want tail, traversed in bottom
    right = right[1:]  # don't want head, traversed in left

    return left + bottom + right


def dfs_children_only(node):
    """Traverse only last childrens."""
    nodes = []
    if node:
        if not node.left and not node.right:  # only append when reaching leafs
            nodes.append(node.data)
        nodes.extend(dfs_children_only(node.left))
        nodes.extend(dfs_children_only(node.right))
    return nodes


def dfs_left_nodes(node):
    """Return left nodes, with head reserve order."""
    nodes = []
    if node:
        nodes.append(node.data)
        nodes.extend(dfs_left_nodes(node.left))  # find all left nodes
    return nodes


def dfs_right_nodes(node):
    """Return right nodes, no head no tail, reverse order."""
    nodes = []
    if node:
        nodes.append(node.data)
        nodes.extend(dfs_right_nodes(node.right))  # find all right nodes
    return nodes


if __name__ == "__main__":
    head = Node(20)
    head.left = Node(10)
    head.left.left = Node(5)
    head.left.right = Node(15)
    head.right = Node(30)
    head.right.left = Node(25)
    head.right.right = Node(35)
