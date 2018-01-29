# Reverse a singly linked list.


class LinkedList(object):
    """Simple linked list class."""

    def __init__(self, val):
        """."""
        self.next = None
        self.val = val


def reverse(head):
    """LC 206, recursion approach."""
    if not head or not head.next:
        return head
    tail = head.next
    head.next = None
    new_head = reverse(tail)  # all val except last one points to None
    tail.next = head  # link all val's next to itself
    return new_head


if __name__ == '__main__':
    l1 = LinkedList(1)
    l1.next = LinkedList(2)
    l1.next.next = LinkedList(3)
    l1.next.next.next = LinkedList(4)
    l1.next.next.next.next = LinkedList(5)
