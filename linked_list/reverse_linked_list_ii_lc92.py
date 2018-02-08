# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.


class LinkedList(object):
    """Simple linked list class."""

    def __init__(self, val):
        """."""
        self.next = None
        self.val = val


def reverse_partial(head, m, n):
    """."""
    p1, p2 = head, head
    for _ in range(m - 1):
        p1 = p1.next
    for _ in range(n - 1):
        p2 = p2.next

    while p1 != p2:
        p1 = p1.next

