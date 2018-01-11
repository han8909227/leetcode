# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


class Node(object):
    """Simple node class."""

    def __init__(self, data):
        """."""
        self.data = data
        self.left = None
        self.right = None


def serialize(node):
    """Bst => list."""
    nodes = []
    if node:  # pre order traversal
        nodes.append(node.data)
        nodes.extend(serialize(node.left))
        nodes.extend(serialize(node.right))
    else:
        nodes.append(None)
    # return ''.join(nodes)  # concat into str
    return nodes


def deserialize(nums):
    """List => bst."""
    val = nums.pop(0)
    if val is None:
        return None
    node = Node(int(val))
    node.left = deserialize(nums)  # traverse all left node of head and their children
    node.right = deserialize(nums)  # traverse all right node of head and their children
    return node  # return the head


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
