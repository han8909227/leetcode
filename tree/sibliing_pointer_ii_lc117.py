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


# a more elagent solution..
def second_connect2(root):
    """LC 117."""
    head = None
    pre = None
    curr = root
    while curr:
        while curr:
            if curr.left:
                if pre:
                    pre.next = curr.left
                else:
                    head = curr.left
                pre = curr.left

            if curr.right:
                if pre:
                    pre.next = curr.right
                else:
                    head = curr.right
                pre = curr.right
            curr = curr.next
        curr = head
        pre = None
        head = None


if __name__ == "__main__":
    head = Node(20)
    head.left = Node(10)
    head.left.left = Node(5)
    head.left.right = Node(15)
    head.right = Node(30)
    head.right.left = Node(25)
    head.right.right = Node(35)
