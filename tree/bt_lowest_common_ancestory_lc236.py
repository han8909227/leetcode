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


def lowest_common_ancestor_no_parent_pointer(root, n1, n2):
    """Return the lowest ancestor of node 1 and node2."""
    if not verify_ancestor(root, n1) or not verify_ancestor(root, n2):
        return None  # if not n1,n2 not children of the root

    # now we know n1,n2 both are at least children of the root
    return ancestor_helper(root, n1, n2)


def ancestor_helper(root, n1, n2):
    """."""
    if root is None or root is n1 or root is n2:
        return root.data
    # when node on different side => current rootf is the lowest ancestor
    if verify_ancestor(root.left, n1) != verify_ancestor(root.left, n2):
        return root.data
    # passed the above if means n1,n2 still on same side => determine side
    child_side = root.left if verify_ancestor(root.left, n1) else root.right
    # recursive go down the tree
    return ancestor_helper(child_side, n1, n2)


def verify_ancestor(root, node):
    """Verify if the node is a desent of the root(passed in node)."""
    if root is None:  # stop perculate if end of tree
        return False
    if root is node:
        return True
    # perculate down the tree to match node
    return verify_ancestor(root.left, node) or verify_ancestor(root.right, node)


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
