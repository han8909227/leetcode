# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.


class LinkedList(object):
    """Simple linked list class."""

    def __init__(self, val):
        """."""
        self.next = None
        self.val = val


def pair_swap(head):
    """LC 24."""
    prev = LinkedList(None)
    prev.next = head
    p1 = head
    p2 = head.next
    result_head = head.next
    while p2.next:
        p1 = p1.next
        p2 = p2.next.next
        p1.next = prev.next
        prev.next = p1
        p1 = p1.next
        p2 = p2.next
        prev = prev.next

    return result_head


if __name__ == '__main__':
    ll = LinkedList(1)
    ll.next = LinkedList(2)
    ll.next.next = LinkedList(3)
    ll.next.next.next = LinkedList(4)
    ll.next.next.next.next = LinkedList(5)
    ll.next.next.next.next.next = None
