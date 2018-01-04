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


def pre_order(node):
    """Traverse nodes using pre-order traversal."""
    nodes = []
    if node:
        nodes.append(node.data)
        nodes.extend(pre_order(node.left))
        nodes.extend(pre_order(node.right))
    return nodes


def zigzag_traversal(head):
    """Traverse tree zig zag level pattern."""
    left = pre_order(head.left)
    right = pre_order(head.right)
    result = [head.data]
    n = 1
    alt = 1
    while left:
        try:
            if alt % 2:
                temp = []
                for _ in range(n):
                    temp.append(left.pop(0))
                for _ in range(n):
                    temp.append(right.pop(0))
                for _ in range(n * 2):
                    result.append(temp.pop())
            else:
                for _ in range(n):
                    result.append(left.pop(0))
                for _ in range(n):
                    result.append(right.pop(0))
            n *= 2
            alt += 1
        except IndexError:
            break
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
    head.right.right.left = Node(38)
    head.left.left.left = Node(2)
    head.left.left.right = Node(8)
    head.left.right.left = Node(12)
    head.left.right.right = Node(18)
