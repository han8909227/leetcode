
# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?


class LinkedList(object):
    """Simple linked list class."""

    def __init__(self, val):
        """."""
        self.next = None
        self.val = val


def detect_cycle(head):
    """LC 141."""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next  # slow iterating slower pase
        fast = fast.next.next  # fast in going faster pase
        if fast == slow:
            return True  # there is an cycle
    return False
