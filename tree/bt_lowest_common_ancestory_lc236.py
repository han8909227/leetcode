# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
# Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


class Node(object):
    """Simple node class."""

    def __init__(self, data):
        """."""
        self.data = data
        self.left = None
        self.right = None


def lowest_ancestor(n1, n2):
    """Return the lowest ancestor of node 1 and node2."""
    depth_diff = depth(n1) - depth(n2)














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
