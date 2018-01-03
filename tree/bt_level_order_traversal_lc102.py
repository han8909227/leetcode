# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
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


def level_traversal(head):
    """Level traverse the tree."""
    left = pre_order(head.left)  # node left of head
    right = pre_order(head.right)  # nodes right of head
    result = [head.data]  # result should have head itself
    n = 1
    while left:  # since left is append first no left means no right in bst
        try:
            for _ in range(n):  # pop(0) deque n times on each side each level, entire level is n*2 nodes
                result.append(left.pop(0))
            for _ in range(n):
                result.append(right.pop(0))
        except IndexError:  # if actual node amt is < possible nodes(ended) => break
            break
        n *= 2  # double n since possible node increase n * 2 for each level each side
    return result


if __name__ == "__main__":
    head = Node(20)
    head.left = Node(10)
    head.left.left = Node(5)
    head.left.right = Node(15)
    head.right = Node(30)
    head.right.left = Node(25)
    head.right.right = Node(35)
