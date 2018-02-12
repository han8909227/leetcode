# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?


class LinkedList(object):
    """Simple linked list class."""

    def __init__(self, val):
        """."""
        self.next = None
        self.val = val


def detect_cycle_ii(head):
    """LC 142."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # cycle = True
            node = head
            while node != slow:  # now the head and slow are x+z apart, target know is in between them and we knowfrom derivation we know x = z
                node = node.next  # move node through x
                slow = slow.next  # move slow through z
            return node  # node = slow = node where cycle begin
    return None
