# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


class Node(object):
    """Simple node class."""

    def __init__(self, data):
        """."""
        self.data = data
        self.left = None
        self.right = None


def zigzag_traversal(head):
    """Zig zag traverse through the tree."""
    if head is None:
        return []
    result, curr = [], [head]
    count = 0
    while curr:
        next_level, vals = [], []  # mt both starting new level
        for node in curr:  # for all node in curr level
            vals.append(node.data)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        curr = next_level  # perculate down level
        if not count % 2:  # alternate order between each level (zig zag)
            result.append(vals)  # vals = all val in single level
        else:
            result.append(vals[::-1])
        count += 1
    return result


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
