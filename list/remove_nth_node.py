# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.


# Definition for singly-linked list.
class ListNode(object):
    """."""

    def __init__(self, x=0):
        """."""
        self.val = x
        self.next = None


# two pass approach
def remove_nth_from_end(head, n):
    """Remove nth node from the end of singly linked list."""
    temp = ListNode()
    temp.next = head
    count = 0
    pointer = head
    while pointer:
        pointer = pointer.next
        count += 1

    pointer = temp
    for _ in range(count - n):
        pointer = pointer.next  # move pointer to node before deleting node
    result = pointer.next.val
    pointer.next = pointer.next.next  # removing connection to del node
    print('deleted node with val ' + str(result))

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
